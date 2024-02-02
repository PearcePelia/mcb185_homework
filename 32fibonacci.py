# 32fibonacci by Pearce Pelia 

def fibonacci(x):
	x1 = -1
	x2 = 1
	for i in range(x):
		total = x1 + x2
		x1 = x2
		x2 = total
		print(total)
		
fibonacci(9)

# def fibonacc(n)
