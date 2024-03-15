#82transfac by Pearce Pelia 

import gzip
import re
import sys
import json


with gzip.open(sys.argv[1], 'rt') as fp:
	transfac = []
	record = {}
	for line in fp:
		line = line.rstrip()
		if line.starts('ID'):
			record['ID'] = line.split()[1]
		elif line.starts('PO'):
			record['pwm'] = []
		elif re.search('\d+', line[0]):
			num = line.split()[1:]
			record['pwm'].append({
				'A': num[0], 
				'C': num[1], 
				'G': num[2], 
				'T': num[3]})
		elif line.starts('//'):
			transfac.append(record)
			record = {}

print(json.dumps(transfac, indent=4))