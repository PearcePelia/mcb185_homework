# 45dndstats.py by Pearce pelia CoAuthor: Lisa Yuan

import random

#3D6
 
limit = 10000
total1 = 0
total2 = 0
total3 = 0
total4 = 0

for i in range(limit):
	for j in range(3):
		total1 += random.randint(1, 6)
		
#3D6r1
for i in range(limit):
	for j in range(3):
		d1 = random.randint(1, 6)
		if d1 == 1:
			d1 = random.randint(1, 6)
		total2 += d1
		
#3D6x2
for i in range(limit):
	for j in range(3):
		dice1 = random.randint(1, 6)
		dice2 = random.randint(1, 6)
		if dice1 > dice2:
			total3 += dice1
		else:
			total3 += dice2

#4D6d1
for i in range(limit):
	for j in range(4):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		d3 = random.randint(1, 6)
		d4 = random.randint(1, 6)
		min_dice = d1
		if d2 < min_dice:
			min_dice = d2
		if d3 < min_dice:
			min_dice = d3
		if d4 < min_dice:
			min_dice = d4
	total4 += (d1 + d2 + d3 + d4) - min_dice

print(f'#3D6 - {total1 / limit}%')
print(f'#3D6r1 - {total2 / limit}%')
print(f'#3D6x2 - {total3 / limit}%')
print(f'#4D6d1 - {total4 / limit}%')