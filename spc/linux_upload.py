import sys
import requests
import getpass
import pickle

def upload():
	client1 = requests.session()
	url= "http://127.0.0.1:8000/accounts/login/"
	url1="http://127.0.0.1:8000/upload/upload/"
	client1.get(url)
	csrftoken = client1.cookies['csrftoken']
	desc= input("Description : ")
	add= input("File Address : ")
	file =open(add,'rb')
	file_name = "login_info.p"
	file_login = open(file_name,'rb')
	data=pickle.load(file_login)
	a=data["Username"]
	b=data["Password"]

	login_data = {
		'username': a,
		'password': b,
		'submit': 'login',
		'csrfmiddlewaretoken':csrftoken
	}
	
	q=client1.post(url,data=login_data)

	if (q.content[100] != 115):
		print("Invalid Request")
		return False
	csrftoken = client1.cookies['csrftoken']

	doc={
		'document' : file

	}

	lols= {
		'description' : desc,
		'location' : add,
		'submit': 'Upload',
		'csrfmiddlewaretoken':csrftoken
	}
	r=client1.post(url1,data=lols, files=doc)

upload()
