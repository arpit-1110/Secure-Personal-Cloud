import sys
import requests
import getpass
import pickle
import os

try:
	file_name = "server_info.p"
	file = open(file_name,'rb')
	dicti = pickle.load(file)
	server = dicti['server_url']
	file.close()
except:
	print("first add a url of server")
	exit()

file_name = "login_info.p"
file = open(file_name,'rb')
d = pickle.load(file)
file.close()

user = d['Username']
passwd = d['Password']

client = requests.session()
url=server + "api/v1/rest-auth/login/"

login_data = {
	'username': user,
	'password': passwd,
}

r = client.post(url, data=login_data)

dicti = r.json()



path = d['path']
parent_id = d['parent_id']

flag = False

url = server + "api/v1/folderlist/"+str(parent_id)+"/"
r = client.get(url)
temp = r.json()
infolist = temp["folderlist"]

inpdir = input("name of the folder: ")

if inpdir == "..":
	parent_id = temp['parent']
	a = path.split("/")
	a = a[0:-1]
	path = "/".join(a)
	flag = True
	print("goes here")

else:	
	for info in infolist:
		if info["name"] == inpdir:
			flag = True
			path = path+"/"+inpdir
			parent_id = info["id"]
			break

if flag == True:
	d['path'] = path
	d['parent_id'] = parent_id
	file = open("login_info.p",'wb')
	pickle.dump(d,file)
	file.close()
else:
	print("No such directories")















