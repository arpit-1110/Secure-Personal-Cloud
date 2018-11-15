w=$(grep -wc "alias spc='bash ~/Secure-Personal-Cloud/spc/linux_client.sh'" ~/.bashrc)
if [[ $w -eq 0 ]] ; then 
	echo "alias spc='bash ~/Secure-Personal-Cloud/spc/linux_client.sh'" | tee -a ~/.bashrc
fi
