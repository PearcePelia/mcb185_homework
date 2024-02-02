# 33triples.py by Pearce pElia 

for a in range(1, 100):
	for b in range(a, 100):
		c = (a ** 2 + b ** 2) ** 0.5
		if c == c // 1: print(a, b, c)
