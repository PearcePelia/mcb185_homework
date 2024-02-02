# 30demo.py by Pearce Pelia

i = 0
while True:
	i = i + 1
	print('hey' , i)
	if i == 3: break
	
i = 0 # where to start
while i < 3: #how many
	print(i) 
	i = i + 1 #incrament 
print('final value of i is', i) #

for i in range(1, 6): print(i)
	
for char in 'hello':
	print(char)

seq = 'GAATTC' # what you want 
for nt in seq: #naming
	print(nt) #printing
	
for nt1 in 'ACGT':
	for nt2 in 'ACGT':
		if nt1 == nt2: print(nt1, nt2, '+1')
		else: print(nt1, nt2, '-1')
	
limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i+1, j+1)
		
