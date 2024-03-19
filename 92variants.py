#92variants.py by Pearce Pelia and CoAuthor Yutong Ji

import argparse
import gzip

parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
arg = parser.parse_args()
print('comparing', arg.gff, arg.vcf)

tp_ranges = {}
with gzip.open(arg.gff, 'rt') as fp:
	for ln in fp:
		ln = ln.split()
		ch = ln[0]
		tp = ln[2]
		strt = int(ln[3])
		stp = int(ln[4])
		if ch not in tp_ranges: tp_ranges[ch] = []
		tp_ranges[ch].append({
			'tp': tp,
			'st': strt,
			'stp': stp})

with gzip.open(arg.vcf, 'rt') as fp:
	for ln in fp:
		ln = ln.split()
		ch = ln[0]
		loc = int(ln[1])
		tps = []
		for rng in tp_ranges[ch]:
			if loc >= rng['st'] and loc <= rng['stp'] and rng['tp'] not in tps:
				tps.append(rng['tp'])
		if tps:
			print(f"{ch}\t{loc}\t{','.join(tps)}")