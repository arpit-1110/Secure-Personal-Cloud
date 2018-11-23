import pickle
from os.path import expanduser
import os

path = input('enter directory path you want to observe: ')

if path[0] == '~' :
	path = expanduser("~") + path[1:]
elif len(path) > 5 :
	if path[:5] != '/home' :
		path = os.getcwd() + "/" + path 
else :
	path = os.getcwd() + "/" + path 
f = open("root_dir.p",'wb+')

pickle.dump({'root_dir' : path},f)
f.close()

