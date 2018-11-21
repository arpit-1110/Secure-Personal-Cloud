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






# url = "http://127.0.0.1:8000/api/v1/createfolder/"+str(parent_id)+"/"

# folder_data = {
# 	'name' : "oh yess second"
# }
# r = client.post(url,data = folder_data)

# print(parent_id)




# os.chdir('test')

# print(os.listdir())

# for f in os.listdir('test'):
# 	file_data = {
# 	'name' : f,
# 	'description' : "first folder through linux",
# 	}

# 	file = open('test/'+f,'rb')

# 	print(file)

# 	upfiles = {
# 		'file' : file,
# 	}
	
	
# 	url = "http://127.0.0.1:8000/api/v1/uploadfile/"+str(parent_id)+"/"
# 	r = client.post(url,data = file_data, files=upfiles)
# 	print(r)
	


# def fileupload(filepath , parent_id):






# if os.path.isdir(path):


# else:

def fileupload(path,name,parent_id):
	file_data = {
	'name' : name,
	'description' : "first recursive folder through linux",
	}

	file = open(path+"/"+name,'rb')

	# print(file)

	upfiles = {
		'file' : file,
	}
	
	
	url = "http://127.0.0.1:8000/api/v1/uploadfile/"+str(parent_id)+"/"
	r = client.post(url,data = file_data, files=upfiles)
	# print(r)


def createfolder(name,parent_id):
	url = "http://127.0.0.1:8000/api/v1/createfolder/"+str(parent_id)+"/"

	folder_data = {
		'name' : name,
	}
	r = client.post(url,data = folder_data)

	# print(parent_id)
	return r.json()["key"]




def recur(path,parent_id):
	for f in os.listdir(path):
		# print(f)
		# print(f)
		# print(os.path.isdir())
		if os.path.isfile(path+"/"+f) == True:
			# print("goes here")
			fileupload(path,f,parent_id)
		elif os.path.isdir(path+"/"+f) == True:
			# print("goes here also")
			key = createfolder(f,parent_id)
			path2 = path + "/" + f
			recur(path2,key)

url="http://127.0.0.1:8000/api/v1/rootfinder/"

r = client.options(url)
parent_id = r.json()["root"]

path = input("Enter the path/name of the folder of file: ")

name = path.split("/")[-1]

if os.path.isdir(path) == True:
	new_parent_id = createfolder(name,parent_id) #extract name from path
	recur(path,new_parent_id)
else:
	file_data = {
	'name' : name,
	'description' : "first recursive folder through linux",
	}

	file = open(path,'rb')

	# print(file)

	upfiles = {
		'file' : file,
	}
	
	
	url = "http://127.0.0.1:8000/api/v1/uploadfile/"+str(parent_id)+"/"
	r = client.post(url,data = file_data, files=upfiles)
	# print(r)

# recur(path,parent_id)





















