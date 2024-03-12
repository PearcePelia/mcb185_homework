#64profinder.py by Pearce Pelia 

import mcb185
import sys
import dogma

final = []

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split() 
	aas = dogma.translate(seq)
	frames = aas.split('*')
	for proteins in frames:
		idx = proteins.find('M')
		if idx != 1:
			save = proteins[idx:]
			saves = save.split('\n')
			for line in saves:
				if len(line) >= int(sys.argv[2]): final.append(line)
	''.join(final)
	for i, line in enumerate(final):
		print(f'>{words[0]}-prot-{i}\n{line}*')