import random 
import sys 

for i in range(5):
	print(random.random())
	
for i in range(50):
	print(random.choice('ACGT'), end='')
print()

for i in range(50):
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end='')
	else: print(random.choice('CG'), end='')
print()

for i in range(3): # how many timesto roll
	print(random.randint(1, 6)) # from what to what 

for i in range(5):
	print(random.gauss(0.0, 1.0))

print(' this line\n has some\n line breaks')

print('a\tb\tcat\tdogma')

print(10, 20, 30, 40, sep='\t')

i = 1
pi = 3.14
print('normal string {i} {pi}')
print(f'formatted string {i} {pi}')
print(f'adding them{i + pi}')

print(f'formatted string {i} {pi:.3f}')
print('logging', file=sys.stderr)

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

