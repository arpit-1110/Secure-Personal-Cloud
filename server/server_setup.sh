name=$(whoami)
tar xf server.tar.gz -C /home/$name/
root_dir="/home/$name/server"

########################### Requirements #########################################
pip3 install django
pip3 install djangorestframework
pip3 install django-filter
pip3 install django-rest-auth
#################################################################################

python3 $root_dir/manage.py makemigrations
python3 $root_dir/manage.py migrate
python3 $root_dir/manage.py runserver 0.0.0.0:8000
