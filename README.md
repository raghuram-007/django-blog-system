
# BlogSphere - Django Blog System

A feature-rich blogging platform built with Django, designed for users to create, manage, and publish blog posts with ease. This system incorporates advanced Django features such as role-based access, email notifications, search functionality, and a user dashboard, making it a robust and professional-grade web application.
## Features

User

🔐 User registration, login, logout, and password reset via email.

📝 Create, edit, delete, and publish posts.

🗂 Categorized posts for easy navigation.

🔍 Search posts by title, content, or category.

📊 Personalized dashboard showing user’s posts.

✉️ Contact form for visitor messages.

📧 Email notifications for new posts.

Admin

⚙️ Access to Django admin panel.

🔑 Role-based redirect ensures secure admin access.

🗂 Manage all posts, categories, and users.
## Folder Structure

Project Structure

django-blog-system/
│
├─ blog/                  # Main app containing models, views, forms, templates
│   ├─ __pycache__/       # Python cache files
│   ├─ templates/         # HTML templates for home, dashboard, posts, etc.
│   ├─ forms.py           # Forms for login, register, contact, post
│   ├─ models.py          # Models: Media, Category, About
│   ├─ views.py           # Views handling requests and business logic
│   └─ urls.py            # URL routing for blog app
│
├─ blogproject/           # Django project folder
│   ├─ __pycache__/       # Python cache files
│   ├─ settings.py        # Project settings
│   ├─ urls.py            # Project URL routing
│   └─ wsgi.py            # WSGI entry point
│
├─ media/                 # Uploaded media files
├─ db.sqlite3             # SQLite database
├─ manage.py              # Django management script
└─ requirements.txt       # Python dependencies

## Author

👤 **Author:** Raghu Ram  
🌐 **GitHub:** [raghuram-007](https://github.com/raghuram-007)  



![Author](https://img.shields.io/badge/Author-Raghu%20Ram-blue?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-raghuram--007-black?style=for-the-badge&logo=github&logoColor=white)

## Badges

Build / Status:

![Python](https://img.shields.io/badge/Python-3.11-blue)


Django Version:

![Django](https://img.shields.io/badge/Django-4.2-green)

MailTesting(Mailtrap.io):
![Mailtrap](https://img.shields.io/badge/Mailtrap-Email%20Testing-00A9E0?style=flat-square&logo=mailtrap)




License:

![License](https://img.shields.io/badge/License-MIT-yellow)


Database:

![Database](https://img.shields.io/badge/Database-SQLite%20/%20MySQL-orange)


Frontend:

![Frontend](https://img.shields.io/badge/Frontend-HTML%2CCSS%2CJS-brightgreen%)

![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat-square&logo=bootstrap&logoColor=white)



Last Commit:

![Last Commit](https://img.shields.io/github/last-commit/raghuram-007/Ecommerse-website)


Issues:

![Issues](https://img.shields.io/github/issues/raghuram-007/Ecommerse-website)






## Tech Stack

🐍 Backend: Python, Django

💻 Frontend: HTML, CSS, JavaScript, Bootstrap

🗄️ Database: SQLite / MySQL (your choice)

✉️ Email: Django email framework & Mailtrap.io

📚 Other Libraries & Tools: Django Paginator, JsonResponse, Django forms

## Installation

Follow these steps to set up the project locally:

📂 Clone the repository:
git clone https://github.com/raghuram-007/django-blog-system.git
cd django-blog-system


🐍 Create a virtual environment:

python -m venv venv


⚡ Activate the virtual environment:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


📦 Install dependencies:

pip install -r requirements.txt


🗄️ Configure the database:

Edit settings.py for SQLite (default) or MySQL connection.

Apply migrations:

python manage.py makemigrations
python manage.py migrate


👤 Create a superuser (optional for admin access):

python manage.py createsuperuser


🌐 Run the development server:

python manage.py runserver


🔗 Open in browser:
Go to http://127.0.0.1:8000/ to view the site.



✉️ Configure Email (optional for notifications):

Add your email settings in settings.py:
visit mailtrap.io create testing smtp
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.example.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "<Mailtrap-user>"
EMAIL_HOST_PASSWORD = "<mailtrap-password>"
DEFAULT_FROM_EMAIL = "<@example-email>"
## Usage

1. Register & Login

📝 Sign Up: New users can register using the signup form.

🔑 Login: Registered users can log in to access their dashboard.

🔒 Password Reset: Forgot your password? Use the password reset feature via email.

Example:

Username: raghu007

Email: your@example.com

Password: ********

2. Create a New Blog Post

🖊️ Navigate to Dashboard → Create Post

Fill in Title, Content, Category, and Image (optional).

Click Publish to make it live.

Example:

Title: My First Django Blog
Category: Django Tutorials
Content: This is an example post explaining how to build a Django blog.

3. Edit or Delete a Post

✏️ Edit: Update content, title, or category via the dashboard.

🗑️ Delete: Remove unwanted posts permanently.

4. Search & Browse

🔍 Search posts by title, content, or category.

📄 Paginated results make browsing smooth and organized.

5. Contact Form

✉️ Visitors can send messages via the Contact Page.

Messages are logged and can be emailed to site admins.

6. Admin Panel

👑 Admin users can log in at /admin to manage all posts, categories, and users.

This section gives a clear, practical example of how someone would actually use blog system,