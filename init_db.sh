
sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE box_django;" 
cd ask
python manage.py syncdb
