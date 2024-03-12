# 70demo.py by Pearce Pelia 

# making a dictionary

d = {'dog': 'woof', 'cat': 'meow'}
print(d)                      
print(d['cat'])               
if 'dog' in d: print(d['dog']) 
if 'rat' in d: print(d['rat'])

# adding to dictionary

d['pig'] = 'oink'
print(d)

d['cat'] = 'mew'
print(d)

for key in d: print(f'{key} says {d[key]}')

for k, v in d.items(): print(k, 'says', v)


print(d.keys(), d.values(), list(d.values()))

import itertools
for nts in itertools.product('ACGT', repeat=2):
	print(nts)