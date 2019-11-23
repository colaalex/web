sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo pip3 install django==2.0.5
sudo pip3 install gunicorn
sudo pip3 install mysqlclient==1.3.12
sudo gunicorn -c /home/box/web/etc/hello.py hello:wsgi_application &
sudo gunicorn -c /home/box/web/etc/gunicorn-django.py ask.wsgi:application &
