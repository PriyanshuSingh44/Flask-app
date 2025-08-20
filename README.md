# Flask Mega-Tutorial: Microblog App
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?logo=flask&logoColor=white)
![Flask-WTF](https://img.shields.io/badge/Flask--WTF-Forms-4B8BBE?logo=wtforms&logoColor=white)
![Flask-Login](https://img.shields.io/badge/Flask--Login-Auth-009688?logo=python&logoColor=white)
![Flask-Mail](https://img.shields.io/badge/Flask--Mail-Email-FF6F00?logo=gmail&logoColor=white)
![Flask-Migrate](https://img.shields.io/badge/Flask--Migrate-DB%20Migrations-006600?logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap%205-Frontend-7952B3?logo=bootstrap&logoColor=white) 
![Flask-Babel](https://img.shields.io/badge/Flask--Babel-i18n%2Fl10n-1d3557?logo=googletranslate&logoColor=white)

This repository contains my progress while following **Miguel Grinberg's Flask Mega-Tutorial**. I am building a full-featured microblogging application step-by-step, implementing features like user authentication, a database, and a responsive UI.

---

### 📚 Chapters Covered So Far

I have successfully completed up to **Chapter 11: Facelift**, which introduces a Bootstrap-based redesign of the application.

* **Chapter 1:** Hello, World!
* **Chapter 2:** Templates
* **Chapter 3:** Web Forms
* **Chapter 4:** Database
* **Chapter 5:** User Logins
* **Chapter 6:** Profile Page and Avatars
* **Chapter 7:** Error Handling
* **Chapter 8:** Followers
* **Chapter 9:** Pagination
* **Chapter 10:** Email Support
* **Chapter 11:** Facelift (Bootstrap 5 UI)
* **Chapter 12:** Dates and Times (moment.js & Flask-Moment)  
* **Chapter 13:** I18n and L10n (Flask-Babel, CLI translation commands)

---

### ⚙️ Features Implemented

The application currently includes the following functionalities:

* **User Management:** Registration, authentication, and user sessions.
* **User Profiles:** Profile pages with avatars (via Gravatar).
* **Posts & Interactions:** Posting and displaying user posts with a followers/following system.
* **Post Pagination:** Pagination for browsing posts.
* **Error Handling:** Custom error pages for 404 and 500 errors.
* **Email Support:** Sending emails for password reset.
* **Frontend:** A responsive and modern UI using Bootstrap 5.
* **Dates and Times:** Time zone–aware timestamps with Flask-Moment (Chapter 12). 
* **Internationalization:** Multi-language support using Flask-Babel, translation markers (`_()`/`_l()`), language catalog management, and translation CLI commands (Chapter 13).

---

### 🚀 Tech Stack

* **Flask:** A lightweight Python web framework.
* **Flask-WTF:** For handling web forms.
* **Flask-Login:** For managing user sessions and authentication.
* **Flask-Mail:** For email support.
* **Flask-Migrate** & **SQLAlchemy:** For database migrations and object-relational mapping (ORM).
* **Flask-Moment:** Client-side timestamps with moment.js (Dates & Times).
* **Flask-Babel:** Internationalization & localization (I18n & L10n).
* **Bootstrap 5:** For frontend styling and UI components.

---

### ▶️ How to Run Locally

Follow these steps to get the application up and running on your local machine.

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
    cd <your-repo-name>
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Linux/macOS
    source venv/bin/activate
    # On Windows
    venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set environment variables:**

    ```bash
    # On Linux/macOS
    export FLASK_APP=microblog.py
    export FLASK_ENV=development

    # On Windows
    set FLASK_APP=microblog.py
    set FLASK_ENV=development
    ```

5.  **Initialize the database:**

    ```bash
    flask db upgrade
    ```

6.  **Run the application:**

    ```bash
    flask run
    ```

---

### 📌 Notes

This is a work-in-progress repository. As I continue the tutorial, I will add more features, including APIs, background jobs, testing, and deployment.
