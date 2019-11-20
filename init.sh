sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
# i'm not sure how to do it correctly but now i launched with gunicorn -c etc/hello.py hello:wsgi_application
# sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
# sudo /etc/init.d/gunicorn restart 
#sudo /etc/init.d/mysql start
