#65transmembrane.py by Pearce Pelia 

import sys
import mcb185
import dogma

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	success = False
	for i in range(0, 30 -8 + 1):
		sp = seq[i:i+8]
		spave = 0.0		
		for i in sp:
			spave += dogma.kyte_doolittle(i)
			spave = spave / 8		
		if spave >= 2.5 and 'P' not in sp:
			for j in range(31, len(seq) -11 +1):
				region = seq[j:j+11]
				regionave = 0
				for k in region:
					regionave += dogma.kyte_doolittle(k)
					regionave = regionave / 11
				if regionave >= 2.0 and 'P' not in region:
					success = True
					break
		if success == True:
			print(defline)
			break