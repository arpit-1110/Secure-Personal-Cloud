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


# key = 'pass'

# TWOen(key, 'Capture.PNG')
# TWOde(key, 'Capture.PNG.enc', 'random.png')