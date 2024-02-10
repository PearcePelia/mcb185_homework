#43randomdna by pearce pelia

import random

for i in range(3):
	print(f'>seq-{i + 1}')
	for j in range(random.randint(50, 60)):
		print(random.choice('ACGT'), end='')
	print()
	
	