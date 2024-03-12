# 62skewer.py by Pearce Pelia 

import sys
import dogma
import mcb185

file = sys.argv[1]  
wsize = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(file):
	for i in range(0, len(seq) - wsize):
		window = seq[i:i + wsize]
		comp = dogma.gc_comp(window)
		skew = dogma.gc_skew(window)
		
for defline, seq in mcb185.read_fasta(file):
	initialwindow = seq[0:wsize]
	types = 'ATCG'
	numbs = []
	for nt in types:
		numbs.append(0)
	for nt in initialwindow:
		idx = types.index(nt)
		numbs[idx] += 1
	comp = (numbs[2] + numbs[3]) / wsize
	skew = (numbs[3] - numbs[2]) / (numbs[3] + numbs[2])

	for i in range(0, len(seq) - wsize):
		idx = types.index(seq[i])
		numbs[idx] -= 1
		inx = types.index(seq[i + wsize])
		numbs[inx] += 1
		comp = (numbs[2] + numbs[3]) / wsize
		if numbs[3] + numbs[2] == 0: skew = 0
		else: skew = (numbs[3] - numbs[2]) / (numbs[3] + numbs[2])