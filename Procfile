web: gunicorn quote_management.wsgi --log-file -
worker: python manage.py celery worker
celery_beat: python manage.py celery beat