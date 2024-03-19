#84splicesites by Pearce Pelia and CoAuthor Yutong Ji

import gzip
import sys
import mcb185

def pwm_list(pwm, ac, id, site):
	print('AC', ac)
	print('XX')
	print('ID', id)
	print('XX')
	print('DE', site)
	print('PO	 A	 C	 G	 T')
	for i, cnts in enumerate(pwm):
		print(f'{i+1:<8}', end='')
		for nt in 'ACGT':
			print(f'{pwm[i][nt]:<8}', end='')
		print()
	print('XX')
	print('//')

chseqs = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	chid = defline.rstrip().split()[0]
	chseqs[chid] = seq

with gzip.open(sys.argv[2], 'rt') as fp:
	introns = []
	for line in fp:
		ln = line.rstrip().split()
		ch = ln[0]
		tp = ln[2]
		strt = int(ln[3])
		stp = int(ln[4])
		strd = ln[6]
		if tp != 'intron': continue
		introns.append((ch, strt, stp, strd))
	print(introns)

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

for ch, strt, stp, strd in introns:
	if strd == '+':
		donseq = chseqs[ch][strt - 1:strt + 5]
		accseq = chseqs[ch][stp - 7:stp]
	else:
		donseq = mcb185.anti_seq(chseqs[ch][stp - 6:stp])
		accseq = mcb185.anti_seq(chseqs[ch][strt - 1:strt + 6])
	for i, nt in enumerate(donseq):
		if 'N' in nt: continue
		don[i][nt] += 1
	for i, nt in enumerate(accseq):
		if 'N' in nt: continue
		acc[i][nt] += 1

pwm_list(don, 'Matrix 1', sys.argv[1].split('/')[3][0:-6], 'Splice Donor Site')
pwm_list(acc, 'Matrix 2', sys.argv[1].split('/')[3][0:-6], 'Splice Acceptor Site')