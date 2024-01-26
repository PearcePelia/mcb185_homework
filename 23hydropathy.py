# 23hydropathy.py by Pearce Pelia done


def hydropathy(aa):
	if aa == 'A': return 1.8
	if aa == 'C': return 2.5
	if aa == 'D': return -3.5
	if aa == 'E': return -3.5
	if aa == 'F': return 2.8
	if aa == 'G': return -0.4
	if aa == 'H': return -3.2
	if aa == 'I': return 4.5
	if aa == 'K': return -3.9
	if aa == 'L': return 3.8
	if aa == 'M': return 1.9
	if aa == 'N': return -3.5
	if aa == 'P': return -1.6
	if aa == 'Q': return -3.5
	if aa == 'R': return -4.5
	if aa == 'S': return -0.8
	if aa == 'T': return -0.7
	if aa == 'V': return 4.2
	if aa == 'W': return -0.9
	if aa == 'Y': return -1.3
		
print(hydropathy('A'))
print(hydropathy('C'))
print(hydropathy('D'))
print(hydropathy('B'))
