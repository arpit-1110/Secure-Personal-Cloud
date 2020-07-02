import os
import random
import struct
import sys
from Crypto.Cipher import AES
import hashlib
import getpass

def AESen(key, in_filename, out_filename=None, chunksize=64*1024) :
	if not out_filename:
		out_filename = in_filename + '.enc'
	iv = os.urandom(16)
	encryptor = AES.new(key, AES.MODE_CBC, IV=iv)
	filesize = os.path.getsize(in_filename)
	with open(in_filename, 'rb') as infile:
		with open(out_filename, 'wb') as outfile:
			# outfile.write(struct.pack('<Q', filesize))
			outfile.write(iv)
			data = infile.read()
			if len(data)%16 != 0 :
				temp = ' '*(16-len(data)%16)
				temp = temp.encode('utf-8')
				data += temp 
			outfile.write(encryptor.encrypt(data))
			# while True :
			# 	chunk = infile.read(chunksize)	
			# 	# print(16 - len(chunk)%16)
			# 	if len(chunk) == 0:
			# 		break
			# 	elif len(chunk) % 16 != 0:
			# 		temp = ' ' * (16 - len(chunk)%16)
			# 		chunk = chunk + temp.encode('utf-8')
			# 	outfile.write(encryptor.encrypt(chunk))

def AESde(key, in_filename, out_filename=None, chunksize=24*1024):
	if not out_filename:
		out_filename = os.path.splitext(in_filename)[0]

	with open(in_filename, 'rb') as infile:
	    # origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
	    iv = infile.read(16)
	    decryptor = AES.new(key, AES.MODE_CBC, iv)
	    # print(iv)
	    with open(out_filename, 'wb') as outfile:
	    	data = infile.read()
	    	outfile.write(decryptor.decrypt(data))
	        # while True:
	        #     chunk = infile.read(chunksize)
	        #     if len(chunk) == 0:
	        #         break
	        #     outfile.write(decryptor.decrypt(chunk))

	        # outfile.truncate(origsize)

from twofish import Twofish 

def TWOen(key, in_filename, out_filename=None, chunksize=16) :
	key = key.encode('utf-8')
	key = Twofish(key)
	if not out_filename :
		out_filename = in_filename + '.enc'
	with open(in_filename, 'rb') as infile :
		with open(out_filename, 'wb') as outfile :
			while True :
				chunk = infile.read(chunksize)
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0 :
					temp = ' '*(16 - len(chunk)%16)
					chunk += temp.encode('utf-8')
				outfile.write(key.encrypt(chunk))

def TWOde(key, in_filename, out_filename=None, chunksize=16) :
	key = key.encode('utf-8')
	key = Twofish(key)
	if not out_filename :
		out_filename = in_filename[:-4]
	with open(in_filename, 'rb') as infile :
		with open(out_filename, 'wb') as outfile :
			while True :
				chunk = infile.read(chunksize)
				if len(chunk) == 0 :
					break 
				outfile.write(key.decrypt(chunk))



from Crypto.Cipher import DES3 
from Crypto import Random 

def DES3en(key, in_filename, out_filename=None, chunk_size=24*1024) :
	if not out_filename :
		out_filename = in_filename + '.enc'
	iv = Random.new().read(DES3.block_size)
	encryptor = DES3.new(key, DES3.MODE_CBC, iv) 
	filesize = os.path.getsize(in_filename)
	with open(in_filename, 'rb') as infile:
		with open(out_filename, 'wb') as outfile:
	# outfile.write(struct.pack('<Q', filesize))
			outfile.write(iv)
			data = infile.read()
			if len(data)%8 != 0 :
				temp = ' '*(8-len(data)%8)
				temp = temp.encode('utf-8')
				data += temp 
			outfile.write(encryptor.encrypt(data))


def DES3de(key, in_filename, out_filename=None, chunk_size=24*1024) :
	if not out_filename :
		out_filename = in_filename[:-4]
	with open(in_filename, 'rb') as infile:
		# origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
		iv = infile.read(8)
		decryptor = DES3.new(key, DES3.MODE_CBC, iv)
		with open(out_filename, 'wb') as outfile:
			data = infile.read()
			outfile.write(decryptor.decrypt(data))



# key = 'pass'

# TWOen(key, 'Capture.PNG')
# TWOde(key, 'Capture.PNG.enc', 'random.png')

# password = 'random'
# key = hashlib.sha256(password.encode('utf-8')).hexdigest()
