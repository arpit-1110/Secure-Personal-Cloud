import sys
import requests
import getpass
import pickle

try:
	file_name = "server_info.p"
	file = open(file_name,'rb')
	dicti = pickle.load(file)
	server = dicti['server_url']
	file.close()
except:
	print("first add a url of server")
	exit()

try:
	file_name = "login_info.p"
	file = open(file_name,'rb')
	d = pickle.load(file)
except:
	print("already logged out")
	file_name = "login_info.p"
	file = open(file_name,'wb')
	d = dict()
	pickle.dump(d,file)
	file.close()




if d == dict():
	print("already logged out")
else:
	client = requests.session()
	url=server + "/api/v1/rest-auth/logout/"

	r = client.post(url)
	dicti = r.json()
	print(dicti['detail'])

	file.close()

	file_name = "login_info.p"
	file = open(file_name,'wb')
	d = dict()
	pickle.dump(d,file)
	file.close()


