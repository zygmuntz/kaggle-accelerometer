'extract intervals between measurements from the training set'
'ignore intervals between different devices'

import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]

i_f = open( input_file )
o_f = open( output_file, 'wb' )

reader = csv.reader( i_f )

headers = reader.next()

n = 0

line = reader.next()
timestamp = float( line[0] )
device = line[4]

for line in reader:
	new_timestamp = float( line[0] )
	new_device = line[4]
	
	if new_device == device:
		interval = int( new_timestamp - timestamp )
		o_f.write( str( interval ) + "\n" )

	timestamp = new_timestamp
	device = new_device
	
	n += 1
	if n % 100000 == 0:
		print n
		
		
		