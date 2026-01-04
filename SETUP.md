# Aid-NSU Setup Guide

This is a Django-based project and does not require npm or Node.js.

## Requirements

- Python 3.8 or higher
- Django 4.2.11
- Django REST Framework 3.14.0

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run database migrations:
```bash
python3 manage.py migrate
```

3. Create a superuser (optional):
```bash
python3 manage.py createsuperuser
```

4. Run the development server:
```bash
python3 manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## Project Structure

- `aidnsu/` - Main project settings
- `base/` - Main application with models, views, and templates
- `static/` - Static files (CSS, JavaScript, images)
- `templates/` - HTML templates
- `db.sqlite3` - SQLite database

## Notes

- This project does NOT use npm. All JavaScript and CSS are served as static files through Django.
- The development server runs on Python/Django, not Node.js.
