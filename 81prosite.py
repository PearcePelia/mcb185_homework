#81prosite.py by Pearce Pelia 
import mcb185
import sys
import re

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H', seq): print(defline)