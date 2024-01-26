#21quadratic.py by Pearce Pelia done

import math
import sys

def quad(a, b, c):
	discrim = b**2 - 4*a*c
	if discrim >= 0:
		x1 = (-b + math.sqrt(discrim)) / (2*a)
		x2 = (-b - math.sqrt(discrim)) / (2*a)
		return x1, x2
	if discrim < 0:
		sys.exit("N/A")
		
print(quad(1, -3, 2))
print(quad(2, 3, 1))
print(quad(1, 0, -1))