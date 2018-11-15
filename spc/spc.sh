cmd=$1
# echo $cmd
if [[ $cmd = "upload" ]] ; then 
	python3 ~/Secure-Personal-Cloud/spc/linux_upload.py
	# echo upload
elif [[ $scmd = "login" ]]; then
 	python3 ~/Secure-Personal-Cloud/spc/linux_client.py
fi
