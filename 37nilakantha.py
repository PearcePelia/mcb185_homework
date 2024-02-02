#37nilakantha by Pearce Pelia 

def nila(number):
	pi = 3.0
	sign = 1

	for n in range(1, number):
		denom = 2 * n * (2 * n + 1) * (2 * n + 2)
		order = 4 / denom
		pi = pi + sign * order 
		sign = sign + (-1)
	return pi

print(nila(2))
print(nila(4))
print(nila(6))