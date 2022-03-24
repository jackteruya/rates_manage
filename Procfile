web: gunicorn quote_management.wsgi --log-file -
worker: python manage.py celery worker
celery_beat: celery -A quote_management beat --scheduler django_celery_beat.schedulers:DatabaseScheduler