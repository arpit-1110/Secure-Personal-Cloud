if [[ $1 == "login" ]] ; then
	python3 ~/Secure-Personal-Cloud/spc/linux_client.py 
elif [[ $1 == "logout" ]]; then
	python3 ~/Secure-Personal-Cloud/spc/linux_logout.py 
elif [[ $1 == "upload" ]]; then
	python3 ~/Secure-Personal-Cloud/spc/linux_upload.py 
fi 
