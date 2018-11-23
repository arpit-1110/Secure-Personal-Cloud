import sys
import requests
import getpass
import pickle
import hashlib
import os
import time


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

url = "http://127.0.0.1:8000/api/v1/get_time_info/"
r = client.get(url)
time_info = r.json()
# print(time_info)

if (int(time_info['allowed']) == 1) or (int(time_info['allowed']) == 0 and time.time() - float(time_info['time']) > 30):
	#sync kar lo
	url = "http://127.0.0.1:8000/api/v1/update_time_info/"
	data = { 'sync_allowed' : '0' , 'timestamp' : str(time.time())}
	r = client.post(url,data = data)
	# print(r.json())
	

	os.system("python3 sync.py")


	data = { 'sync_allowed' : '1' , 'timestamp' : str(time.time())}
	r = client.post(url,data = data)
	# print(r.json())

else:
	print("Another Sync is going on, try again later")
	exit()






# elif int(time_info['allowed']) == 0:
# 	if time.time() - float(time_info['time']) > 30:
# 		print("deadlock condition")
# 		url = "http://127.0.0.1:8000/api/v1/update_time_info/"
# 		data = { 'sync_allowed' : '0' , 'timestamp' : str(time.time())}
# 		r = client.post(url,data = data)
# 		# print(r.json())
# 		a = 1
# 		print("sync in progress")
# 		for i in range(1,100000000):
# 			a = a+1
# 		data = { 'sync_allowed' : '1' , 'timestamp' : str(time.time())}
# 		r = client.post(url,data = data)
# 		# print(r.json())
# 		#sync kar lo

# 	else:
		










