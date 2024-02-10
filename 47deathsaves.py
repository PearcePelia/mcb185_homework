#47deathsaves.py by Pearce Pelia

import random 

limit = 10000
die = 0
stable = 0 
revive = 0
for i in range(limit):
	success = 0
	failure = 0
	while True:
		rolls = random.randint(1, 20)
		if rolls == 1:
			failure += 2
			if failure >= 3:
				die += 1
				break
		elif rolls < 10:
			failure += 1
			if failure >= 3:
				die += 1
				break
		elif rolls == 20:
			success += 1
			if success >= 1:
				revive += 1
				break 
		else: 
			success += 1
			if success >= 3:
				stable += 1
				break
print(f'The probability of one dying, being stable, and revived after {limit} trails is:')				
print(f'dying - {die / limit}%')
print(f'stable - {stable / limit}%')
print(f'revive - {revive / limit}%')	
	
			