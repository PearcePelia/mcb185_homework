#60demo.py by Pearce Pelia 

import mcb185
import sys

A = 0
C = 0
G = 0
T = 0
N = 0


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0 
	for nt in seq:
		if nt == 'A': A += 1
		elif nt == 'C': C += 1
		elif nt == 'G': C += 1
		elif nt == 'T': C += 1
		else: N += 1
	print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))
	
nts = 'ACGTN'
counts = []
for i in range(len(nts)): counts.append(0)
for nt in seq:
	if nt == 'A': counts[0] += 1
	elif nt == 'C': counts[1] += 1
	elif nt == 'G': counts[2] += 1
	elif nt == 'T': counts[3] += 1
	else: counts[4] += 1
print(name, end='\t')
for n in counts: print(f'{n/len(seq):.4f}', end = '\t')
print()

counts = [0] * len(nts)
for nt in seq:
	idx = nts.find(nt)
	counts[idx] += 1
print(name, end='\t')
for n in counts: print(f'{n/len(seq):.4f}', end='\t')
print()

nts = 'ACGTN' # should really be defined outside the loop
print(name, end='\t')
for nt in nts:
	print(seq.count(nt) / len(seq), end='\t')
print()	