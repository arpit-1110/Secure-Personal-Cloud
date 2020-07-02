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
passwd1 = getpass.getpass("Password : ")
passwd2 = getpass.getpass("Re-enter the Password : ")


client = requests.session()
url=server + "api/v1/rest-auth/registration/"

login_data = {
	'username': user,
	'password1': passwd1,
	'password2' : passwd2,
}

r = client.post(url, data=login_data)
dicti = r.json()

# print(dicti)

try:
	dicti['key']
	print("Signed up successfully")
except:
	print("Enter proper credentials")



