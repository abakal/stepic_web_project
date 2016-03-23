
sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE qa_db;" 
cd ask
python manage.py syncdb
