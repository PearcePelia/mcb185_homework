# 72kmercount.py by Pearce Pelia 

import sys
import mcb185
import itertools

k = int(sys.argv[2])
kcnt = {}
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k + 1):
		kmer = seq[i:i+k]
		if kmer not in kcnt: kcnt[kmer] = 0
		kcnt[kmer] += 1
	for nts in itertools.product('ACGT', repeat = k):
		kmer = ''.join(nts)
		if kmer in kcnt: print(kmer, kcnt[kmer])
		else:            print(kmer, 0)