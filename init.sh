sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
# i dunno how it starts some troubles
. env/bin/activate
sudo gunicorn -c /home/box/web/etc/hello.py hello:wsgi_application &
sudo gunicorn -c /home/box/web/etc/gunicorn-django.py ask.wsgi:application &
