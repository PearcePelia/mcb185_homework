#83kozak.py by Pearce Pelia and CoAuthor Yutong Ji
import gzip
import sys
import json
import mcb185

with gzip.open(sys.argv[1], 'rt') as fp:
	fullseq = []
	coords = []
	seqs = False
	for line in fp:
		line = line.rstrip()
		if line.starts('VERSION'):
			line = line.split()
			ac = line[1]
		elif '/organism=' in line:
			line =line.replace('"', '').split('=')
			id = line[1]
		elif line.starts('CDS'): 
			if 'join' in line: continue
			elif 'complement' in line:
				startidx = line.find('(') + 1
				stopidx = line.find(')')
				start, stop = line[startidx:stopidx].split('..')
				coords.append((int(start), int(stop), '-'))
			else:
				start, stop = line.split()[1].split('..')
				coords.append((int(start), int(stop), '+'))	
		elif line.starts('ORIGIN'):
			seqs = True
			continue
		if seqs:
			line = line.split()
			for seq in line[1:]:
				fullseq.append(seq)						
	fullseq = ''.join(fullseq).upper()

kozaks = []
for i in range(14):
	kozaks.append({
		'A': 0,
		'C': 0,
		'G': 0,
		'T': 0})
		
for start, stop, strd in coords:
	if strd == '-':
		kozak = fullseq[stop - 5: stop + 9]
		kozak = mcb185.anti_seq(kozak)
	else:
		kozak = fullseq[start - 10: start + 4]
	for i, nt in enumerate(kozak):
		kozaks[i][nt] += 1

print('AC', ac)
print('XX')
print('ID', id)
print('XX')
print('DE PWM for the Kozak consensus for E.coli')
print('PO	 A	 C	 G	 T')
for i, cnts in enumerate(kozaks):
	print(f'{i+1:<8}', end='')
	for nt in 'ACGT':
		print(f'{kozaks[i][nt]:<8}', end='')
	print()
print('XX')
print('//')