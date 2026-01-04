# Aid-NSU Setup Guide

This is a Django-based study collaboration application.

## Requirements

- Python 3.10 or higher
- Django 4.2.11
- Django REST Framework 3.14.0
- PostgreSQL (for production with Supabase) or SQLite (for development)

## Development Setup

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

4. Collect static files:
```bash
python3 manage.py collectstatic
```

5. Run the development server:
```bash
python3 manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## Production Deployment

### Environment Setup

1. Copy `.env.production.example` to `.env.production` and update with your values:
```bash
cp .env.production.example .env
```

2. Set required environment variables:
- `DEBUG=False` - Disable debug mode
- `ALLOWED_HOSTS` - Your domain(s)
- `SECRET_KEY` - A secure random key (use `python3 -c "import secrets; print(secrets.token_urlsafe(50))"`)
- `DATABASE_URL` - PostgreSQL connection string from Supabase

### Supabase Database Setup

1. Create a Supabase account and project
2. Get your PostgreSQL connection string from Supabase dashboard
3. Set `DATABASE_URL` in your environment
4. Run migrations on the production database:
```bash
python3 manage.py migrate
```

### Deployment with Gunicorn

```bash
gunicorn aidnsu.wsgi:application --bind 0.0.0.0:8000
```

Or use the included Procfile for platform deployment (Heroku, Railway, etc.)

## Project Structure

- `aidnsu/` - Main Django project settings
- `base/` - Main application (models, views, templates)
- `static/` - Static assets (CSS, JavaScript, images)
- `templates/` - HTML templates
- `staticfiles/` - Collected static files for production
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (development)
- `Procfile` - Process file for cloud deployment

## Security Features

- HTTPS/SSL configured for production
- CSRF protection enabled
- Secure session cookies
- HSTS headers for production
- Content Security Policy
- Database connection pooling
- WhiteNoise for static file serving

## Database Configuration

- Development: SQLite (db.sqlite3)
- Production: PostgreSQL (via Supabase)

The application automatically detects and uses the appropriate database based on the `DATABASE_URL` environment variable.

## Troubleshooting

### Database Connection Issues
- Verify `DATABASE_URL` is correctly formatted
- Check firewall/network access to database
- Ensure database user has proper permissions

### Static Files Not Loading
- Run `python3 manage.py collectstatic --noinput`
- Check `STATIC_ROOT` and `STATIC_URL` configuration

### Secret Key Warning
- Generate a new SECRET_KEY: `python3 -c "import secrets; print(secrets.token_urlsafe(50))"`
- Update in your environment variables
