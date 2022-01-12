python manage.py collectstatic --no-input

python manage.py migrate

waitress-serve --listen=*:8000 --worker-tmp-dir /dev/shm email_script_site.wsgi