import pickle

path = input('enter directory path you want to observe: ')

f = open("root_dir.p",'wb+')

pickle.dump({'root_dir' : path},f)
f.close()

