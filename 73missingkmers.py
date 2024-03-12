# 73missingkmers.py by Pearce Pelia and CoAuthor Yutong Ji

import sys
import mcb185
import itertools

for k in range(1, 10): 
	kcount = {}
	for deflin, seq in mcb185.read_fasta(sys.argv[1]):
		counts = 0
		for i in range(len(seq) -k + 1):
			kmer = seq[i:i+k]
			if kmer not in kcount:
				kcount[kmer] = 0
			kcount[kmer] += 1
		antiseq = mcb185.anti_seq(seq)
		for i in range(len(antiseq) -k + 1):
			kmer = antiseq[i:i+k]
			if kmer not in kcount:
				kcount[kmer] = 0
			kcount[kmer] += 1
		for nts in itertools.product('ACGT', repeat = k):
			kmer = ''.join(nts)
			if kmer in kcount: 
				continue
			else:
				print(kmer, 0)
				zero_counts += 1
	if zero_counts != 0:
		print('k = ' k, counts)
		break