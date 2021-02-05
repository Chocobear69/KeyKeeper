python manage.py migrate
python manage.py collectstatic
gunicorn key_keeper.wsgi:application --bind=0.0.0.0:8080 --worker=6