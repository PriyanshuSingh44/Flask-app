import os 
os.environ['DATABASE_URL'] = 'sqlite://'

from datetime import datetime, timezone, timedelta
import unittest
from hashlib import md5
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User()
        u.username = 'priyanshu'
        u.email = 'priyanshu@example.com'
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_avatar(self):
        u = User()
        u.username = 'john'
        u.email = 'john@example.com'
        self.assertEqual(u.avatar(128), 'https://www.gravatar.com/avatar/'+md5('john@example.com'.lower().encode('utf-8')).hexdigest()+'?d=identicon&s=128')
    
    def test_follow(self):
        u1 = User()
        u1.username = 'priyanshu'
        u1.email = 'priyanshu@example.com'
        u2 = User()
        u2.username = 'john'
        u2.email = 'john@example.com'
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        following = db.session.scalars(u1.following.select()).all()
        followers = db.session.scalars(u2.followers.select()).all()
        self.assertEqual(following, [])
        self.assertEqual(followers, [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.following_count(), 1)
        self.assertEqual(u2.followers_count(), 1)
        u1_following = db.session.scalars(u1.following.select()).all()
        u2_followers = db.session.scalars(u2.followers.select()).all()
        self.assertEqual(u1_following[0].username, 'john')
        self.assertEqual(u2_followers[0].username, 'priyanshu')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.following_count(), 0)
        self.assertEqual(u2.followers_count(), 0)

    def test_follow_posts(self):
        # create four users
        u1 = User()
        u1.username = 'john'
        u1.email = 'john@example.com'
        
        u2 = User()
        u2.username = 'susan'
        u2.email = 'susan@example.com'
        
        u3 = User()
        u3.username = 'mary'
        u3.email = 'mary@example.com'
        
        u4 = User()
        u4.username = 'david'
        u4.email = 'david@example.com'
        
        db.session.add_all([u1, u2, u3, u4])

        # create four posts
        now = datetime.now(timezone.utc)
        # create posts with explicit timestamps for testing order
        p1 = Post()
        p1.body = "post from john"
        p1.timestamp = now + timedelta(seconds=1)
        p1.author = u1
        
        p2 = Post()
        p2.body = "post from susan"
        p2.timestamp = now + timedelta(seconds=4)
        p2.author = u2
        
        p3 = Post()
        p3.body = "post from mary"
        p3.timestamp = now + timedelta(seconds=3)
        p3.author = u3
        
        p4 = Post()
        p4.body = "post from david"
        p4.timestamp = now + timedelta(seconds=2)
        p4.author = u4
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # setup the followers
        u1.follow(u2)
        u1.follow(u4)
        u2.follow(u3)
        u3.follow(u4)
        db.session.commit()

        #check the following posts of each user
        f1 = db.session.scalars(u1.following_posts()).all()
        f2 = db.session.scalars(u2.following_posts()).all()
        f3 = db.session.scalars(u3.following_posts()).all()
        f4 = db.session.scalars(u4.following_posts()).all()
        self.assertEqual([p.body for p in f1], ["post from susan", "post from david", "post from john"])
        self.assertEqual([p.body for p in f2], ["post from susan", "post from mary"])
        self.assertEqual([p.body for p in f3], ["post from mary", "post from david"])
        self.assertEqual([p.body for p in f4], ["post from david"])

if __name__ == '__main__':
    unittest.main(verbosity=2)