name=$(whoami)
tar xf spc.tar.gz -C /home/$name/
########################### Requirements #########################################
pip3 install pycrypto
pip3 install django
pip3 install twofish
pip3 install djangorestframework
pip3 install markdown
pip3 install django-filter
pip3 install wget
##################################################################################

root_dir="/home/$name/spc"

w=$(grep -wc "alias spc='python3 $root_dir/host.py'" ~/.bashrc)
if [[ $w -eq 0 ]] ; then 
	echo "alias spc='python3 $root_dir/host.py'" | tee -a ~/.bashrc
fi

