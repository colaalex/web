sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
source env/bin/activate
sudo gunicorn -c /home/box/web/etc/hello.py hello:wsgi_application
sudo gunicorn -c /home/box/web/etc/gunicorn-django.py ask.wsgi:application
#sudo /etc/init.d/mysql start
