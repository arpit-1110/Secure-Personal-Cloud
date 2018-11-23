import os
import hashlib
import sys
import requests
import getpass
import pickle

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

# print(d)


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, 'rb') as file2:
	    for chunk in iter(lambda: file2.read(4096), b""):
	        hash_md5.update(chunk)
    return hash_md5.hexdigest()

def listdir_nohidden(path):
	try:
	    for f in os.listdir(path):
	    	if not f.startswith('.'):
	        	yield f
	except:
		for f in os.listdir():
			if not f.startswith('.'):
				yield f



# walk_dir = 'mysite'
# for root, subdirs, files in os.walk(walk_dir):
#     print('--\nroot = ' + root)
#     list_file_path = os.path.join(root, 'my-directory-list.txt')
#     print('list_file_path = ' + list_file_path)

#     with open(list_file_path, 'wb') as list_file:
#         for subdir in subdirs:
#             print('\t- subdirectory ' + subdir)

#         for filename in files:
#             file_path = os.path.join(root, filename)

#             print('\t- file %s (full path: %s)' % (filename, file_path))


path = ""

with open("root_dir.p",'rb') as f :
	# print(pickle.load(f))
	root_dir = pickle.load(f)['root_dir']



os.chdir(root_dir)

pathlist = []
mdlist = []

def clientrecur(path):
	try:
		lst = listdir_nohidden(path)
	except:
		lst = listdir_nohidden('')

	if path == "":
		for l in lst:
			if os.path.isdir(l):
				clientrecur(l)
			else:
				pathlist.append(l)
				mdlist.append(md5(l))

	else:
		for l in lst:
			if os.path.isdir(path+"/"+l):
				recur(path+"/"+l)
			else:
				pathlist.append( path+"/"+l )
				mdlist.append(md5(path+"/"+l))

clientrecur("")
# print(pathlist)
# print(mdlist)


#server ka list ===================================================

serverpathlist = []
servermdlist = []

parent_id = d['parent_id']


def folderlist(parent_id):
	url = "http://127.0.0.1:8000/api/v1/folderlist/"+str(parent_id)+"/"
	r = client.get(url)
	infolist = r.json()["folderlist"]
	return infolist

def filelist(parent_id):
	url = "http://127.0.0.1:8000/api/v1/filedownload/"+str(parent_id)+"/"
	r = client.get(url)
	infolist = r.json()['info']
	return infolist

# print(folderlist(parent_id))
# print(filelist(parent_id))


server_path = ''

def serverrecur(path,parent_id):
	folderkalist = folderlist(parent_id)
	filekalist = filelist(parent_id)

	
	for folder in folderkalist:
		if path == "":
			newpath = folder['name']
		else:
			newpath = path + "/" + folder['name']
		# print("foldeer is: " + str(folder))

		serverrecur(newpath,folder['id'])

	for file in filekalist:
		if path == "":
			newpath = file['name']
		else:
			newpath = path + "/" + file['name']

		serverpathlist.append(newpath)
		servermdlist.append(file['md5sum'])

serverrecur('',parent_id)

# print(servermdlist)
# print(serverpathlist)



if sorted(servermdlist) == sorted(mdlist):
	print("perfectly synced")
	# exit()

extrafilesonserver = []
extrafilesonclient = []
intersectionchanged = []
intersectionunchanged = []

# extrafilesonserver.sort()
# extrafilesonclient.sort()
# intersectionchanged.sort()
# intersectionunchanged.sort()

for i in range(len(serverpathlist)):
	if serverpathlist[i] not in pathlist:
		extrafilesonserver.append(serverpathlist[i])
	else:
		if servermdlist[i] == mdlist[pathlist.index(serverpathlist[i])]:
			intersectionunchanged.append(serverpathlist[i])
		else:
			intersectionchanged.append(serverpathlist[i])


for i in range(len(pathlist)):
	if pathlist[i] not in serverpathlist:
		extrafilesonclient.append(pathlist[i])

# print(extrafilesonserver)
# print(extrafilesonclient)
# print(intersectionchanged)
# print(intersectionunchanged)


if len(extrafilesonserver) != 0 :
	print('Extra files on server are: ')
	for i in extrafilesonserver :
		print('\t' + str(i))
else :
	print('No extra files are present on server')

if len(extrafilesonclient) != 0 :
	print('Extra files on client are: ')
	for i in extrafilesonclient :
		print('\t' + str(i))
else :
	print('No extra files are present on client')

if len(intersectionchanged) != 0 :
	print('Files changed are: ')
	for i in intersectionchanged :
		print('\t' + str(i))
else :
	print('No changed files')

if len(intersectionunchanged) != 0 :
	print('Files Unchanged are: ')
	for i in intersectionunchanged :
		print('\t' + str(i))
else :
	print('No unchanges files')

	# print()

























