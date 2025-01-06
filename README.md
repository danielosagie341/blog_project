# Django Blog Project

A full-featured blog application built with Django, featuring user authentication, profile management, and blog post creation.

## Features

- User registration and authentication
- User profile management with profile pictures
- Blog post creation, editing, and deletion
- Responsive design using Tailwind CSS

## Setup and Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- PostgreSQL

### Local Development Setup

1. Clone the repository
```bash
git clone <your-repository-url>
cd blog_project

Create and activate a virtual environment

bashCopypython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

bashCopypip install -r requirements.txt

Create a .env file in the root directory and add your environment variables:

CopySECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=your_database_host
DATABASE_PORT=5432

Run migrations

bashCopypython manage.py migrate

Create a superuser

bashCopypython manage.py createsuperuser

Run the development server

bashCopypython manage.py runserver
The application will be available at http://localhost:8000
Deployment
Deploying to Render

Create a new Web Service on Render
Link your GitHub repository
Configure the following settings:

Build Command: pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
Start Command: gunicorn blog_project.wsgi:application


Add environment variables in Render's dashboard
Deploy!

Environment Variables for Production
Required environment variables:

SECRET_KEY
DATABASE_URL
DEBUG (set to False)
ALLOWED_HOSTS

Project Structure
Copyblog_project/
├── blog_project/        # Project settings directory
├── core/               # Main app directory
├── templates/          # HTML templates
├── static/            # Static files
├── media/             # User-uploaded files
├── requirements.txt   # Project dependencies
└── manage.py          # Django management script
Testing
Run tests with:
bashCopypython manage.py test



This README:
1. Explains what the project is
2. Details setup instructions for both development and production
3. Lists key features
4. Provides deployment instructions
5. Includes information about testing and contributing
6. Shows the project structure
