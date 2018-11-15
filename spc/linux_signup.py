import sys
import requests
import getpass
import pickle


user = input("Username : ")
passwd = getpass.getpass("Password : ") 
checkpass = getpass.getpass ("Re-enter Password : ")   


def mylogin(a,b,c):
	client = requests.session()
	url="http://127.0.0.1:8000/accounts/signup/"
	client.get(url)
	csrftoken = client.cookies['csrftoken']
	login_data = {
		'username': a,
		'password1': b,
		'password2' : c,
		'submit': 'Sign up',
		'csrfmiddlewaretoken':csrftoken
	}

	r = client.post(url, data=login_data)
	if (r.content[100] != 105):
		# print(r.content[100])
		print("Invalid Signup")
		return False
	else :
		file_name = "login_info.p"
		file = open(file_name,'wb')
		d = {'Username' : a, 'Password' : b}
		pickle.dump(d,file)
		file.close()
		return True
	



mylogin(user,passwd, checkpass)	