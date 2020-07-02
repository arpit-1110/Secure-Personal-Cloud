# `pip install pycrypto`

import hashlib
from Crypto.Cipher import DES3 
from Crypto import Random 
import os 
import struct

password = 'random'
key = hashlib.sha256(password.encode('utf-8')).hexdigest()

def DES3en(key, in_filename, out_filename=None, chunk_size=24*1024) :
	if not out_filename :
		out_filename = in_filename + '.enc'
	iv = Random.new().read(DES3.block_size)
	encryptor = DES3.new(key, DES3.MODE_OFB, iv) 
	filesize = os.path.getsize(in_filename)
	with open(in_filename, 'rb') as infile:
	        with open(out_filename, 'wb') as outfile:
	            outfile.write(struct.pack('<Q', filesize))
	            outfile.write(iv)
	            while True :
	            	chunk = infile.read(chunk_size)
	            	if len(chunk) == 0 :
	            		break 
	            	elif len(chunk)%8 != 0 :
	            		temp = ' '*(8 - len(chunk)%8)
	            		chunk += temp.encode('utf-8')
            		outfile.write(encryptor.encrypt(chunk))


def DES3de(key, in_filename, out_filename=None, chunk_size=24*1024) :
	if not out_filename :
		out_filename = in_filename[:-4]
	with open(in_filename, 'rb') as infile:
	    origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
	    iv = infile.read(8)
	    decryptor = DES3.new(key, DES3.MODE_OFB, iv)
	    with open(out_filename, 'wb') as outfile:
	        while True:
	            chunk = infile.read(chunk_size)
	            if len(chunk) == 0:
	                break
	            outfile.write(decryptor.decrypt(chunk))

	        outfile.truncate(origsize)


DES3en(key[:16], 'Capture.PNG')	
DES3de(key[:16], 'Capture.PNG.enc', 'phoo.png')
