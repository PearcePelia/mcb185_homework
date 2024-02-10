#46savingthrows.py by Pearce Pelia
#not correct 

import random
limit = 1000
advantage = 0
disadvantage = 0
result1 = 0

for i in range(limit):
	for j in range(1):
	d1 = random.randint(1, 20)
	d2 = random.randint(1, 20)
	if d1 > d2: 
		result1 += d1
	else: 
		result1 += d2
	
#DC of 10
for i in range(limit):
	print(random.randint(1, 2))
	if result2 == 1: print(advantage)
	elif result2 == 2: print(disadvantage)

#DC of 15
for i in range(limit):
	print(random.randint(1, 2))
	if result3 == 1: print(advantage)
	elif result3 == 2: print(disadvantage)
	
print(f'DC of 5 - {result1 / limit}')
print(f'DC of 10 - {result2 / limit}')
print(f'DC of 15 - {result3 / limit}')
