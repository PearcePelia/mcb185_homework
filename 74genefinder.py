#74genefinder.py by Pearce Pelia and CoAuthor Yutong Ji

import sys
import mcb185

min_length = int(sys.argv[2])		

def gene_finder(seq):
	coords = {}
	start_cdn = 'ATG'
	stop_cdn = ['TAA', 'TAG', 'TGA']
	for frame in range(3):
		i = frame
		while i < len(seq):
			if seq[i:i+3] == start_cdn:
				start_idx = i
				for j in range(i + 3, len(seq), 3):
					if seq[j:j+3] in stop_cdn:
						stop_idx = j
						if stop_idx - start_idx >= min_length:
							coords[start_idx] = stop_idx + 2
							i = stop_idx
						break
			i += 3
	return coords

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	rev = mcb185.anti_seq(seq)
	coordinationsplus = gene_finder(seq)
	coordinationsminus = gene_finder(rev)
	for k, v in coordinationsplus.items():
		print(k, v, '+')
	for k, v in coordinationsminus.items():
		kminus = len(seq) - k - 1
		vminus = len(seq) - v - 1
		print(vminus, kminus, '-')