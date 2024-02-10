# 44randompi by pearce PElia

import random
import math

inside = 0
total = 0

while True:
	x = random.random()
	y = random.random()
	d = math.sqrt(x**2 + y**2)
	
	if d <= 1:
		inside += 1
	total += 1
	
	print(4 * inside / total)