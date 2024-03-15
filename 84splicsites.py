#84splicesites by Pearce Pelia and CoAuthor Yutong Ji

import mcb185
import json
import gzip
import sys
import re

fasta = sys.argv[1] 
gff = sys.argv[2] 



def pwm_list(pwm, ac, id, desc):
	print('AC', ac)
	print('XX')
	print('ID', id)
	print('DE', desc)
	print('PO   A   C   G   T')
	nts = 'ACGT'
	print('PO', end='\t')
	for nt in nts: 
		print(f'{nt:<8}', end='') 
	print()
	
	for i, dictionary in enumerate(pwm):
		print(i+1, end='\t')
		for nt, n in dictionary.items():
			print(f'{n:<8}', end=' ')
   		
		print()	
	print('XX')	
	print('//')
	
	
chrom = {}
for defline, seq in mcb185.read_fasta(fasta):
	chromID = defline.split()[0]
	chrom[chromID] = seq
introns = []
with gzip.open(gff, 'rt') as fp:
	for line in fp:
		f = line.split('\t') 
		c = f[0]
		t = f[2] 
		b = int(f[3]) -1 
		e = int(f[4]) -1 
		n = f[5]
		s = f[6] 
		if t != 'intron': continue
		if n == '.': continue
		n = float(n)
		introns.append((c, b, e, n, s))

don =[]
acc = []
for i in range(6):
	don.append({
		'A': 0,
		'C': 0,
		'G': 0,
		'T': 0})
for i in range(7):
	acc.append({
		'A': 0,
		'C': 0,
		'G': 0,
		'T': 0})
		
for c, b, e, n, s in introns:
	if s == "+":
		intronseq = chrom[c][b:e+1]
	else:
		intronseq = mcb185.anti_seq(chrom[c][b:e+1]
	
	dseq = intronseq[0:6]
	for i, nt in enumerate(dseq):
		don[i][nt] += 1 
	
	aseq = intronseq[-7:]
	for i, nt in enumerate(aseq):
		acc[i][nt] += 1
	
		
print_pwm(acc, 'ik001', 'ACC1', 'splice acceptor')
print_pwm(don, 'ik002', 'DON', 'splice acceptor')