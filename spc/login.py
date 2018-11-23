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



user = input("Username : ")
passwd = getpass.getpass("Password : ")    

client = requests.session()
url = server + "/api/v1/rest-auth/login/"

login_data = {
	'username': user,
	'password': passwd,
}

r = client.post(url, data=login_data)
dicti = r.json()

try:
	file_name = "login_info.p"
	file = open(file_name,'wb+')
	dicti["key"]
	url=server+"/api/v1/rootfinder/"
	r = client.get(url)
	parent_id = r.json()["root"]
	d = {'Username' : user, 'Password' : passwd, 'key' : dicti["key"], 'path' : user, 'parent_id' : parent_id }
	pickle.dump(d,file)
	file.close()
	print("Successfully Logged in")
	

except:
	d = dict()
	pickle.dump(d,file)
	file.close()
	print("Invalid Login")







	



























