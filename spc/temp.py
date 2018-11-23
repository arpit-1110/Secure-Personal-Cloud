import pickle

with open('pass.p', 'wb') as f :
	data = {}
	data['md5'] = 'null'
	data['option'] = 'null'
	pickle.dump(data, f)