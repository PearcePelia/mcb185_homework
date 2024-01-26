# 25entropy.py by Pearce Pelia 

import math 
import sys 

def shannonentropy(a, c, g, t):
	total = a + c + g + t
	assert(total > 0)
	aprob = a / total 
	cprob = c / total
	gprob = g / total
	tprob = t / total
	aexp = 0
	cexp = 0
	gexp = 0
	texp = 0 
	if aprob > 0: aexp = aprob * math.log2(aprob)	
	if cprob > 0: cexp = cprob * math.log2(cprob)	
	if gprob > 0: gexp = gprob * math.log2(gprob)	
	if tprob > 0: texp = tprob * math.log2(tprob)	
	
	entropy = -(aexp + cexp + gexp + texp)
	return entropy
	
print(shannonentropy(1, 2, 3, 4))
print(shannonentropy(3, 5, 7, 9))
print(shannonentropy(2, 4, 6, 8))
print(shannonentropy(0, 0, 1, 0))	#if its zero
