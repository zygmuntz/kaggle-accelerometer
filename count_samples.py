"""
count samples for each device in the train file
output device_id,no_samples
usage: count_samples.py train.csv samples_per_device.csv
"""

import sys
import csv

print __doc__

input_file = sys.argv[1]
output_file = sys.argv[2]

reader = csv.reader( open( input_file ))
writer = csv.writer( open( output_file, 'wb' ))

# skip headers
reader.next()

prev_device = 0		# device id
no_samples = 0		# reset with each new device
n = 0

for line in reader:
	device = line[4]
	
	if device == prev_device:
		no_samples += 1
		
	elif prev_device is not 0:
		writer.writerow( [ prev_device, no_samples ] )
		print "device %s: %s samples" % ( prev_device, no_samples )
		no_samples = 0
		
	prev_device = device
	
	n += 1
	if n % 100000 == 0:
		print n

# last device		
writer.writerow( [ device, no_samples ] )	
print "device %s: %s samples" % ( device, no_samples )
