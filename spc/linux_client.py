import sys
import requests
import getpass
import pickle


user = input("Username : ")
passwd = getpass.getpass("Password : ")    


def mylogin(a,b):
	client = requests.session()
	url="http://127.0.0.1:8000/accounts/login/"
	client.get(url)
	csrftoken = client.cookies['csrftoken']
	login_data = {
		'username': a,
		'password': b,
		'submit': 'login',
		'csrfmiddlewaretoken':csrftoken
	}

	r = client.post(url, data=login_data)
	if (r.content[100] != 115):
		print("Invalid Login")
		return False
	else :
		file_name = "login_info.p"
		file = open(file_name,'wb')
		d = {'Username' : a, 'Password' : b}
		pickle.dump(d,file)
		file.close()
		return True
	



mylogin(user,passwd)	

# task = input("Task : ")	

























