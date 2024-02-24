#56birthday.py by Pearce Pelia
import random 
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

match = 0
for trial in range(trials):
	birthday = []
	for i in range(people):
		day = random.randint(1, days)
		birthday.append(day)
	birthday.sort()
	for i in range(people - 1):
		if birthday[i] == birthday[i + 1]:
			match += 1
			break
print(match / trials)
	
		
		