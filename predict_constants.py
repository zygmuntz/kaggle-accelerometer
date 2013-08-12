"""
produce an answers file using only samples per device information
usage: predict_constants.py questions.csv samples_per_device.csv answers.csv
AUC 0.80343
"""

print __doc__

import sys, csv

questions_file = sys.argv[1]
input_file = sys.argv[2]		# samples per device file produced with count_samples.py
output_file = sys.argv[3]

# samples per device

reader = csv.reader( open( input_file ))

samples_per_device = {}
sum_of_samples = 0

for line in reader:
	device, samples = line
	samples = int( samples )
	samples_per_device[device] = samples
	sum_of_samples += samples
	
# probs for each device based on number of samples	
	
sum_of_samples = float( sum_of_samples )	
	
device_probs = {}
for d in samples_per_device:
	prob = samples_per_device[d] / sum_of_samples
	device_probs[d] = prob

###

reader = csv.reader( open( questions_file ))
writer = csv.writer( open( output_file, 'wb' ))

headers = reader.next()
writer.writerow( [ 'QuestionId', 'IsTrue' ] )

n = 0

for line in reader:
	q_id, q_sequence, q_device = line

	prob = device_probs[q_device]
	
	writer.writerow( [ q_id, prob ] )
	
	n += 1
	if n % 10000 == 0:
		print n
		
		