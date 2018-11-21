# curl -X POST http://127.0.0.1:8000/api/v1/rest-auth/logout/

import sys
import requests
import getpass
import pickle


file_name = "login_info.p"
file = open(file_name,'rb')
d = pickle.load(file)



if d == dict():
	print("already logged out")
else:
	client = requests.session()
	url="http://127.0.0.1:8000/api/v1/rest-auth/logout/"

	r = client.post(url)
	dicti = r.json()
	print(dicti['detail'])

	file.close()

	file_name = "login_info.p"
	file = open(file_name,'wb')
	d = dict()
	pickle.dump(d,file)
	file.close()


