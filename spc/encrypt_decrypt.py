import os
import random
import struct
import sys
from Crypto.Cipher import AES
import hashlib
import getpass
# password = 'bitch'
password = getpass.getpass()

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024) :
	if not out_filename:
	    out_filename = in_filename + '.enc'
	    # iv = 16 * '\x00'
	    iv = os.urandom(16)
	    # iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
	    encryptor = AES.new(key, AES.MODE_CBC, IV=iv)
	    filesize = os.path.getsize(in_filename)

	    with open(in_filename, 'r') as infile:
	        with open(out_filename, 'wb') as outfile:
	            outfile.write(struct.pack('<Q', filesize))
	            outfile.write(iv)

	            while True:
	                chunk = infile.read(chunksize)
	                if len(chunk) == 0:
	                    break
	                elif len(chunk) % 16 != 0:
	                    chunk += ' ' * (16 - len(chunk) % 16)

	                outfile.write(encryptor.encrypt(chunk))
# key='0123456789abcdef'

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
	if not out_filename:
		out_filename = os.path.splitext(in_filename)[0]

	with open(in_filename, 'rb') as infile:
	    origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
	    iv = infile.read(16)
	    decryptor = AES.new(key, AES.MODE_CBC, iv)

	    with open(out_filename, 'w') as outfile:
	        while True:
	            chunk = infile.read(chunksize)
	            if len(chunk) == 0:
	                break
	            outfile.write(decryptor.decrypt(chunk))

	        outfile.truncate(origsize)

# decrypt_file(key[:16], 'temp.txt.enc', 'myfile')

password = password.encode('utf-8')
key = hashlib.sha256(password).hexdigest()
# print(key)
# encrypt_file(key[:16], 'temp.txt')

if sys.argv[1] == "encrypt" :
	encrypt_file(key[:16], sys.argv[2])

elif sys.argv[1] == "decrypt" :
	enc_file = sys.argv[2]
	decrypt_file(key[:16], enc_file, enc_file[:-4])

else :
	print("Invalid option")