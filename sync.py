import sys
import requests
import getpass
import pickle
import hashlib
import os
import wget

 
stoc_for_all = False
ctos_for_all = False
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, 'rb') as file2:
	    for chunk in iter(lambda: file2.read(4096), b""):
	        hash_md5.update(chunk)
    return hash_md5.hexdigest()

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

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

with open("root_dir.p",'rb') as f:
	root_dir = pickle.load(f)['root_dir']

#download wala part ========================================================

os.chdir(root_dir)
# client = requests.session()
currpath = ""

url="http://127.0.0.1:8000/api/v1/rootfinder/"

r = client.options(url)
parent_id = r.json()["root"]

def filedownload(path,name,infofile):
	url = "http://127.0.0.1:8000/files/download/?name="+infofile
	filename = wget.download(url,out=path)
	try:
		if path == '':
			os.rename(filename,name)
		else:
			os.rename(filename,path+"/"+name)
	except:
		print("shit")
		pass




def recur(path,id):
	url = "http://127.0.0.1:8000/api/v1/filedownload/"+str(id)+"/"
	# print()
	global stoc_for_all
	global ctos_for_all
	r = client.get(url)
	# print(r)
	infolist = r.json()

	for info in infolist['info']:
		try:
			dircontent = os.listdir(path)
		except:
			dircontent = os.listdir()
		# print("info dicti is :"+str(info))
		name = info['name']
		# name = name.split("/")[-1]
		# print("naam hai :" + name)
		# print(dircontent)

		if (name in dircontent):
			# print(dircontent)
			if path == '':
				iskifile = name
			else:
				iskifile = path+"/"+name
			if md5(iskifile) == info['md5sum']:
				print("haan same hai")
			else:
				print("change ho gaya")

				if stoc_for_all == True:
					filedownload(path,name,info['file'])
				elif ctos_for_all == True:
					print("query is 2 kuchh nahi karna")
				else:

					q = int(input("files confict. You have 4 options: \
											1: Server to your system for this file\
											2: Your system to server for this file\
											3: Server to your system for all files\
											4: Your system to server for all file "))
					if q == 1:
						filedownload(path,name,info['file'])
					elif q == 2:
						print("query is 2 kuchh nahi karna")
					elif q == 3:
						filedownload(path,name,info['file'])
						stoc_for_all = True
					else:
						print("query is 2 kuchh nahi karna")
						ctos_for_all = True


		else:
			filedownload(path,name,info['file'])


	url = "http://127.0.0.1:8000/api/v1/folderlist/"+str(id)+"/"
	r = client.get(url)
	# print(r)
	infolist = r.json()["folderlist"]
	# print(infolist)

	for info in infolist:
		try:
			dircontent = os.listdir(path)
		except:
			dircontent = os.listdir()
		if (info['name'] in dircontent):
			name = info["name"]
			folderid = info["id"]
			if path =='':
				folderpath = name
			else:
				folderpath = path + "/" + name
			# os.mkdir(folderpath)
			# print(folderpath)
			recur(folderpath,folderid)
		else:
			name = info["name"]
			folderid = info["id"]
			if path =='':
				folderpath = name
			else:
				folderpath = path + "/" + name
			os.mkdir(folderpath)
			print(folderpath)
			recur(folderpath,folderid)



recur(currpath,parent_id)

#upload wala part ========================================================




def fileupload(path,name,parent_id):
	file = open(path+"/"+name, 'rb')


	file_data = {
	# 'name' : name,
	'md5sum' : md5(path+"/"+name),
	}

	# print(md5(path+"/"+name))

	upfiles = {
		'file' : file,
	}
	
	
	url = "http://127.0.0.1:8000/api/v1/uploadfile/"+str(parent_id)+"/"
	r = client.post(url,data = file_data, files=upfiles)
	return r.json()['status']


def createfolder(name,parent_id):
	url = "http://127.0.0.1:8000/api/v1/createfolder/"+str(parent_id)+"/"

	folder_data = {
		'name' : name,
	}
	r = client.post(url,data = folder_data)

	# print(parent_id)
	return r.json()["key"]




def recur(path,parent_id):
	for f in listdir_nohidden(path):
		if os.path.isfile(path+"/"+f) == True:
			# print("goes here")
			status = fileupload(path,f,parent_id)
			if(status == "yes"):
				print("uploading "+path+"/"+f+"......")
		elif os.path.isdir(path+"/"+f) == True:
			# print("goes here also")
			key = createfolder(f,parent_id)
			path2 = path + "/" + f
			recur(path2,key)

url="http://127.0.0.1:8000/api/v1/rootfinder/"

r = client.options(url)
parent_id = r.json()["root"]


# name = path.split("/")[-1]

# new_parent_id = createfolder(name,parent_id) #extract name from path
recur(root_dir,parent_id)






