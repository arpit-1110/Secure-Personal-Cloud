root_dir="/home/arpit/spc"

if [[ $1 == "login" ]] ; then
	python3 $root_dir/linux_client_api.py 
elif [[ $1 == "logout" ]]; then
	python3 $root_dir/linux_client_logout_api.py 
elif [[ $1 == "upload" ]]; then
	python3 ~/Desktop/Secure-Personal-Cloud/spc/linux_api.py 
fi 
