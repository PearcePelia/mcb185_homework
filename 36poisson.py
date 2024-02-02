#36poisson.py by Pearce Pelia 

import math 

def poisson(n, k):
	prob = (n ** k * math.exp(-n)) / math.factorial(k)
	return prob
	
print(poisson(1, 2))
print(poisson(3, 4))
print(poisson(5, 6))


