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

# try:
# 	file_name = "login_info.p"
# 	file = open(file_name,'wb+')
# 	d = {'Username' : user, 'Password' : passwd, 'key' : dicti["key"], }
# 	pickle.dump(d,file)
# 	file.close()
# except:
# 	d = dict()
# 	pickle.dump(d,file)
# 	file.close()
# 	print("Invalid Login")
# print(d)

path = d['path']
parent_id = d['parent_id']


url = "http://127.0.0.1:8000/api/v1/folderlist/"+str(parent_id)+"/"
r = client.get(url)
infolist = r.json()["folderlist"]

print("Folders: ")
for info in infolist:
	print("   "+info['name'])

print("Files:")

url = "http://127.0.0.1:8000/api/v1/filedownload/"+str(parent_id)+"/"
r = client.get(url)
infolist = r.json()['info']
for info in infolist:
	print("   "+info['name'])










