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


url = server + "api/v1/folderlist/"+str(parent_id)+"/"
r = client.get(url)
infolist = r.json()["folderlist"]

print("Folders: ")
for info in infolist:
	print("   "+info['name'])

print("Files:")

url = server + "api/v1/filedownload/"+str(parent_id)+"/"
r = client.get(url)
infolist = r.json()['info']
for info in infolist:
	print("   "+info['name'])










