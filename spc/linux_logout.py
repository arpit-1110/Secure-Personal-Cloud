import sys
import requests
import getpass
import pickle



def mylogout():
	file_name = "login_info.p"
	file = open(file_name,'wb')
	d = {}
	pickle.dump(d,file)
	file.close()
	return True




mylogout()