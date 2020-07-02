import sys
import requests
import getpass
import pickle
import hashlib
import os
import wget
import time

pass_file = "pass.p"
home_dir = os.getcwd()


try:
	file_name = "server_info.p"
	file = open(file_name,'rb')
	dicti = pickle.load(file)
	server = dicti['server_url']
	file.close()
except:
	print("first add a url of server")
	exit()

def take_pass() :
	passwd = getpass.getpass("Enter the new password: ")
	conf_passwd = getpass.getpass("Again enter the password")
	if passwd != conf_passwd :
		print("Passwords didn't match")
		take_pass()
	return passwd 

def take_option() :
	option = str(input("Enter the method of encryption (AES/DES3/Twofish): "))
	if option != 'AES' and option != 'DES3' and option != 'Twofish' :
		raise Exception("Invalid encryption method")
	return option


# with open()
# print(option)
# passwd = init()
# option = str(input("Enter method of encryption (AES/DES3/Twofish): "))

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
try:
	file_name = "login_info.p"
	file = open(file_name,'rb')
	d = pickle.load(file)
	user = d['Username']
	passwd = d['Password']
except:
	print("First login")
	exit()



client = requests.session()
url=server + "api/v1/rest-auth/login/"

login_data = {
	'username': user,
	'password': passwd,
}

r = client.post(url, data=login_data)

dicti = r.json()

with open("root_dir.p",'rb') as f:
	root_dir = pickle.load(f)['root_dir']

#download wala part ========================================================

url = server + "api/v1/get_time_info/"
r = client.get(url)
time_info = r.json()
# print(time_info)

if (int(time_info['allowed']) == 1) or (int(time_info['allowed']) == 0 and time.time() - float(time_info['time']) > 3):

	url = server + "api/v1/update_time_info/"
	data = { 'sync_allowed' : '0' , 'timestamp' : str(time.time())}
	r = client.post(url,data = data)

#sync starting ============================================================================
	os.chdir(root_dir)
	# client = requests.session()
	currpath = ""

	# url="http://127.0.0.1:8000/api/v1/rootfinder/"

	# r = client.options(url)
	# parent_id = r.json()["root"]
	parent_id = d['parent_id']

	from en_de import AESde
	from en_de import DES3de
	from en_de import TWOde


	def filedownload(path,name,infofile, passwd, option):
		url = server + "files/download/?name="+infofile
		filename = wget.download(url,out=path)
		if option == 'AES' :
			key = hashlib.sha256(passwd.encode('utf-8')).digest()
			AESde(key[:32], filename)
		if option == 'DES3' :
			key = hashlib.sha256(passwd.encode('utf-8')).digest()
			DES3de(key[:16], filename)
		if option == 'Twofish' :
			TWOde(key, filename)
		
		# print('filename' + filename)
		tempfilename = filename.split(".")[0:-1]
		tempfilename = ".".join(tempfilename)
		try:
			os.remove(filename)
			# print('goes here')
		except:
			# print("ahiya")
			pass

		# print("new listdir: ")
		try:
			print(os.listdir(path))
		except:
			print(os.listdir())


		
		if path == '':
			os.rename(tempfilename,name)
		else:
			os.rename(tempfilename,path+"/"+name)
		# print("success")
	




	def recur_download(path,id, passwd, option):
		url = server + "api/v1/filedownload/"+str(id)+"/"
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
					# print("haan same hai")
					pass
				else:
					# print("change ho gaya")

					if stoc_for_all == True:
						filedownload(path,name,info['file'], passwd, option)
					elif ctos_for_all == True:
						pass
						# print("query is 2 kuchh nahi karna")
					else:

						q = int(input("files "+ path + "/" + name + " confict. You have 4 options: \
												1: Server to your system for this file\
												2: Your system to server for this file\
												3: Server to your system for all files\
												4: Your system to server for all file "))
						if q == 1:
							filedownload(path,name,info['file'], passwd, option)
						elif q == 2:
							# print("query is 2 kuchh nahi karna")
							pass
						elif q == 3:
							filedownload(path,name,info['file'], passwd, option)
							stoc_for_all = True
						else:
							# print("query is 2 kuchh nahi karna")
							ctos_for_all = True


			else:
				filedownload(path,name,info['file'], passwd, option)


		url = server + "api/v1/folderlist/"+str(id)+"/"
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
				recur_download(folderpath,folderid, passwd, option)
			else:
				name = info["name"]
				folderid = info["id"]
				if path =='':
					folderpath = name
				else:
					folderpath = path + "/" + name
				os.mkdir(folderpath)
				# print(folderpath)
				recur_download(folderpath,folderid, passwd, option)



	#upload wala part ========================================================


	from enc import enc_upload

	def fileupload(path,name,parent_id, passwd, option):
		# print(passwd)
		# print(option)
		loc = path+"/"+name
		file_data = {
		'name' : name,
		'md5sum' : md5(loc),
		}
		iv = '186DE986FC69F8E47ED692B24D940'
		file = enc_upload(path, name, passwd, option)
		# print(name)
		
		# print(str(file))

		upfiles = {
			# 'name' : name,
			'file' : file,
		}
		
		# print(file_data['name'])
		url = server + "api/v1/uploadfile/"+str(parent_id)+"/"
		r = client.post(url,data = file_data, files=upfiles,timeout = 1000000)
		os.remove(loc+'.enc')
		return r.json()['status']


	def createfolder(name,parent_id):
		url = server + "api/v1/createfolder/"+str(parent_id)+"/"

		folder_data = {
			'name' : name,
		}
		r = client.post(url,data = folder_data)

		# print(parent_id)
		return r.json()["key"]

	def folderlist(parent_id):
		url = server + "api/v1/folderlist/"+str(parent_id)+"/"
		r = client.get(url)
		infolist = r.json()["folderlist"]
		ans = []
		for f in infolist:
			ans.append(f['name'])
		return ans

	def filelist(parent_id):
		url = server + "api/v1/filedownload/"+str(parent_id)+"/"
		r = client.get(url)
		infolist = r.json()['info']
		ans = []
		for f in infolist:
			ans.append({ f['name'] : f['md5sum']})
		return ans




	def recur_upload(path,parent_id, passwd, option):
		filekalist = filelist(parent_id)
		folderkalist = folderlist(parent_id)
		# print(filekalist)
		# print(folderkalist)
		for f in listdir_nohidden(path):
			if os.path.isfile(path+"/"+f) == True:
				# print("goes here")

				temp_dict = {f : str(md5(path+"/"+f))}
				if temp_dict in filekalist:
					# print("same hai don't upload")
					pass
				else:
					status = fileupload(path,f,parent_id, passwd, option)
					if(status == "yes"):
						print("uploading "+path+"/"+f+"......")
			elif os.path.isdir(path+"/"+f) == True:
				# print("goes here also")
				key = createfolder(f,parent_id)
				path2 = path + "/" + f
				recur_upload(path2,key, passwd, option)

	def recur_upload_withoutcheck(path,parent_id, passwd, option):
		print("goes here")
		for f in listdir_nohidden(path):
			if os.path.isfile(path+"/"+f) == True:
				status = fileupload(path,f,parent_id, passwd, option)
				print("updating encryption of "+path+"/"+f+"......")
			elif os.path.isdir(path+"/"+f) == True:
				# print("goes here also")
				key = createfolder(f,parent_id)
				path2 = path + "/" + f
				recur_upload_withoutcheck(path2,key, passwd, option)


	# url="http://127.0.0.1:8000/api/v1/rootfinder/"
	# r = client.options(url)
	parent_id = d['parent_id']

	import shutil

	def init() :
		global parent_id
		global home_dir
		global root_dir
		# print(root_dir)
		os.chdir(home_dir)
		with open(pass_file, 'rb') as f :
			data = pickle.load(f)
		if data['md5'] == 'null' :
			passwd = take_pass()
			with open(pass_file, 'wb') as f :
				pickle.dump({'md5': passwd, 'option' : data['option']}, f)
			# return passwd	
		elif data['option'] == 'null' :
			op = take_option()
			with open(pass_file, 'wb') as f :
				pickle.dump({'md5': data['md5'], 'option' : op}, f)
			# return passwd
		else :
			if len(sys.argv) > 1 :
				with open(pass_file, 'rb') as f :
					data = pickle.load(f)
					prev_passwd = data['md5']
					prev_option = data['option']
				if 'o' in sys.argv[1] :
					op = take_option()
					with open(pass_file, 'wb') as f :
						pickle.dump({'md5': data['md5'], 'option' : op}, f)
				if 'c' in sys.argv[1] :
					passwd = take_pass()
					with open(pass_file, 'wb') as f :
						pickle.dump({'md5' : passwd, 'option' : data['option']}, f)
				with open(pass_file, 'rb') as f :
					data = pickle.load(f)
					new_passwd = data['md5']
					new_option = data['option']
				# os.chdir(root_dir)
				recur_upload_withoutcheck(root_dir,parent_id, new_passwd, new_option)

	init()

	with open(pass_file, 'rb') as f :
		data = pickle.load(f)
	file_passwd = data['md5']
	option = data['option']
	os.chdir(root_dir)
	import time
	recur_download(currpath,parent_id, file_passwd, option)
	time.sleep(0.01)
	recur_upload(root_dir,parent_id, file_passwd, option)

	print("sync done")

	#sync done ====================================================
	url = server + "api/v1/update_time_info/"

	data = { 'sync_allowed' : '1' , 'timestamp' : str(time.time())}
	r = client.post(url,data = data)
	# print(r)


else:
	print("Another sync is going on, please try again later")
	exit()

