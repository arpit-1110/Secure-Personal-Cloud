name=$(whoami)
tar xf client.tar.gz -C /home/$name/
########################### Requirements #########################################
pip3 install pycrypto
pip3 install twofish
pip3 install wget
##################################################################################

root_dir="/home/$name/client"

w=$(grep -wc "alias spc='python3 $root_dir/host.py'" ~/.bashrc)
if [[ $w -eq 0 ]] ; then 
	echo "alias spc='python3 $root_dir/host.py'" | tee -a ~/.bashrc
fi

