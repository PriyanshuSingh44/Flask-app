from flask_wtf import FlaskForm
from flask_babel import _, lazy_gettext as _l
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
import sqlalchemy as sa
from app import db
from app.models import User


class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()]) # type: ignore
    password = PasswordField(_l('Password'), validators=[DataRequired()]) # type: ignore
    remember_me = BooleanField(_l('Remember Me'))  # type: ignore
    submit = SubmitField(_l('Sign In'))   # type: ignore


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()]) # type: ignore
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])  # type: ignore
    password = PasswordField(_l('Password'), validators=[DataRequired()])  # type: ignore
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),EqualTo('password')])  # type: ignore
    submit = SubmitField(_l('Register'))  # type: ignore

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError(_l('Please use a different username.'))  # type: ignore

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError(_l('Please use a different email address.'))  # type: ignore


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])  # type: ignore
    submit = SubmitField(_l('Request Password Reset'))  # type: ignore


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])  # type: ignore
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),EqualTo('password')])  # type: ignore
    submit = SubmitField(_l('Request Password Reset'))  # type: ignore


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])  # type: ignore
    about_me = TextAreaField(_l('About me'),validators=[Length(min=0, max=140)])  # type: ignore
    submit = SubmitField(_l('Submit'))  # type: ignore

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = db.session.scalar(sa.select(User).where(
                User.username == username.data))
            if user is not None:
                raise ValidationError(_l('Please use a different username.'))  # type: ignore


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[ DataRequired(), Length(min=1, max=140)])  # type: ignore
    submit = SubmitField(_l('Submit'))  # type: ignore