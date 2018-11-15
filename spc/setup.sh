w=$(grep -wc "alias spc='bash ~/Secure-Personal-Cloud/spc/spc.sh'" ~/.bashrc)
if [[ $w -eq 0 ]] ; then 
	echo "alias spc='bash ~/Secure-Personal-Cloud/spc/spc.sh'" | tee -a ~/.bashrc
fi
