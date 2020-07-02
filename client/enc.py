from en_de import AESen
from en_de import DES3en
from en_de import TWOen
import hashlib

def enc_upload(path, name, passwd, option) :
	loc = path+"/"+name 
	if option == "AES" :
		key = hashlib.sha256(passwd.encode('utf-8')).digest()
		AESen(key[:32], loc)
	elif option == "DES3" :
		key = hashlib.sha256(passwd.encode('utf-8')).digest()
		DES3en(key[:16], loc)
	elif option == "Twofish" :
		TWOen(passwd, loc)
	else :
		raise Exception("Invalid method of encryption; Try using AES/DES3/Twofish")
	return open(loc+'.enc','rb')
