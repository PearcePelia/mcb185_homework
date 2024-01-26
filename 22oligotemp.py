# 22oligotemp.py by Pearce Pelia done

def oligomt(a, c, g, t):
	length = a+c+g+t
	if length <= 13:
		Tm = (a+t)*2 + (g+c)*4
		return Tm
	else: Tm = 64.9 + 41*(g+c - 16.4) / length
	return Tm
	
print(oligomt(10,10,10,10))
print(oligomt(5,5,5,5))
print(oligomt(1,1,1,1))