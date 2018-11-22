import sys
import requests
import getpass
import pickle
import os

file_name = "login_info.p"
file = open(file_name,'rb')
d = pickle.load(file)
file.close()

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
parent_id = d['parent_id']

flag = False

url = "http://127.0.0.1:8000/api/v1/folderlist/"+str(parent_id)+"/"
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















