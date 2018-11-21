import sys
import requests
import getpass
import pickle

user = input("Username : ")
email = input("Email: ")
passwd1 = getpass.getpass("Password : ")
passwd2 = getpass.getpass("Reenter the Password : ")


client = requests.session()
url="http://127.0.0.1:8000/api/v1/rest-auth/registration/"

login_data = {
	'username': user,
	# 'email' : email,
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
	print("Invalid input")



