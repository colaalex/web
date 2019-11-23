sudo /etc/init.d/mysql start
mysql -uroot -e "create database app;"
mysql -uroot -e "create user 'box'@'localhost' identified by 'Password1!';"
mysql -uroot -e "grant all privileges on app.* to 'box'@'localhost' with grant option;"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate