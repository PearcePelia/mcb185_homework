import random 
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

match = 0

for trial in range(trials):
	cal = []
	for i in range(days):
		cal.append(0)
	for i in range(people):
		bday = random.randint(0, days - 1)
		cal[bday] += 1
		if cal[bday] >= 2:
			match += 1
			break
			
print(match / trials)
	