#71countgff.py by Pearce Pelia 

import gzip
import sys
import gzip
import sys

count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for le in fp:
		if ln.startswith('#'): continue
		f = ln.split()
		feature = f[2]
		if feature not in count: count[feature] = 0
		else:                    count[feature] += 1
for f, n in count.items(): print(f, n)