python manage.py migrate
python manage.py collectstatic
waittress-serve --host=0.0.0.0 --port=8080 --threads=64 --backlog=1000