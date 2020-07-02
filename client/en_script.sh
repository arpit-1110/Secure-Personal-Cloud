action=$1
method=$2
file=$3
pass=$4
echo here
if [[ $method == 'AES' ]]; then
	if [[ $action == "e" ]];  then
		openssl enc -aes-256-cbc -in $file -out "$file.enc" -pass pass:$pass -iv 186DE986FC69F8E47ED692B24D940
	fi
	if [[ $action == "d" ]]; then
		openssl enc -d -aes-256-cbc -in $file -out "${file::-4}" -pass pass:$pass
	fi
elif [[ $method == "RC4" ]]; then
	if [[ $action == "e" ]];  then
		openssl enc -rc4 -in $file -out "$file.enc" -pass pass:$pass
	fi
	if [[ $action == "d" ]]; then
		openssl enc -d -rc4 -in $file -out "${file::-4}" -pass pass:$pass
	fi
elif [[ $method == "DES" ]]; then
	if [[ $action == "e" ]];  then
		openssl enc -des-cbc -in $file -out "$file.enc" -pass pass:$pass
	fi
	if [[ $action == "d" ]]; then
		openssl enc -d -des-cbc -in $file -out "${file::-4}" -pass pass:$pass
	fi
fi
