import sys
import requests
import getpass
import pickle
import os

file_name = "login_info.p"
file = open(file_name,'rb')
d = pickle.load(file)

user = d['Username']
passwd = d['Password']

client = requests.session()
url="http://127.0.0.1:8000/api/v1/rest-auth/login/"

login_data = {
	'username': user,
	'password': passwd,
}

r = client.post(url, data=login_data)

dicti = r.json()

path = d['path']

print(path)