import sys 
import os 
import pickle

def run() :
	flags = sys.argv[1:]
	with open('server_info.p', 'rb') as f :
		data = pickle.load(f)
	# print(flags)
	if 'login' in flags or ('config' in flags and 'edit' in flags) :
		os.system('python3 login.py')
	if 'logout' in flags :
		os.system('python3 logout.py')
	if 'signup' in flags :
		os.system('python3 signup.py')
	if 'ls' in flags :
		os.system('python3 ls.py')
	if 'cd' in flags :
		os.system('python3 cd.py')
	if 'pwd' in flags :
		os.system('python3 pwd.py')
	if 'server' in flags :
		data = data['server_url']
		x = data.split('/')
		x = x[2]
		y = x.split(':')
		print('IP: ' + y[0])
		print('Port: ' + y[1])
	if '-u' in flags or 'status' in flags :
		os.system('python3 status.py')
	if '-v' in flags or '--version' in flags:
		print('1.0.1') 
	if '-o' in flags or 'observe' in flags :
		os.system('python3 observe.py')
	if '-s' in flags or 'sync' in flags :
		os.system('python3 sync.py')
	if '-h' in flags or 'help' in flags :
		os.system('cat manual.txt')
	if '-p' in flags or 'change-pass' in flags :
		os.system('python3 sync.py c')
	if '-c' in flags or 'change-option' in flags :
		os.system('python3 sync.py o') 
if len(sys.argv) > 1 :
	run()
else :
	os.system('cat manual.txt')
