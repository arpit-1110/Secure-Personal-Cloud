import sys
import requests
import getpass
import pickle
import wget
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

try:
	file_name = "login_info.p"
	file = open(file_name,'wb+')
	d = {'Username' : user, 'Password' : passwd, 'key' : dicti["key"]}
	pickle.dump(d,file)
	file.close()
except:
	d = dict()
	pickle.dump(d,file)
	file.close()
	print("Invalid Login")

# os.rmdir(user)


# url = "http://127.0.0.1:8000/api/v1/filedownload/"+str(27)+"/"
# print()
# r = client.get(url)
# print(r)
# infolist = r.json()

# for info in infolist['info']:
# 	url = "http://127.0.0.1:8000/files/download/?name="+info['file']
# 	print(url)
# 	filename = wget.download(url,out=user)

os.mkdir(user)
# client = requests.session()
currpath = user

url="http://127.0.0.1:8000/api/v1/rootfinder/"

r = client.options(url)
parent_id = r.json()["root"]

# print(parent_id)


def recur(path,id):
	url = "http://127.0.0.1:8000/api/v1/filedownload/"+str(id)+"/"
	# print()
	r = client.get(url)
	# print(r)
	infolist = r.json()

	for info in infolist['info']:
		url = "http://127.0.0.1:8000/files/download/?name="+info['file']
		print(url)
		filename = wget.download(url,out=path)

	url = "http://127.0.0.1:8000/api/v1/folderlist/"+str(id)+"/"
	r = client.get(url)
	# print(r)
	infolist = r.json()["folderlist"]
	# print(infolist)

	for info in infolist:
		name = info["name"]
		folderid = info["id"]
		folderpath = path + "/" + name
		os.mkdir(folderpath)
		recur(folderpath,folderid)

recur(user,parent_id)






