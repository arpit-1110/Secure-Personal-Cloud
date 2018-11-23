import pickle

server_url = input("Enter url of server: ")

file_name = "server_info.p"
file = open(file_name,'wb+')
pickle.dump({'server_url' : server_url},file)
file.close()

