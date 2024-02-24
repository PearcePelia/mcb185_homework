import gzip
import sys
import math

gffpath = sys.argv[1]
feature = sys.argv[2]

def mean(vals):
	total = 0
	for val in vals: total += val
	len_mean = total / len(vals)	
	return len_mean

def stdev(vals):
	m = mean(vals)
	varience = 0
	for val in vals: varience += (val - m) ** 2 
	return varience

def median(vals):
	n = len(vals)
	if n % 2 == 0: 
		mid1 = round(n / 2 - 1) # 2
		mid2 = round(n / 2) # 3
		return (vals[mid1] + vals[mid2]) / 2
	else:
		mid = round(n / 2)
		return vals[mid]
		
lengths = []
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		words = line.split()
		if words[2] == feature: 
			beg = int(words[3])
			end = int(words[4])
			length = end - beg + 1
			lengths.append(length)

print(lengths.sort())
count = print(len(lengths))
minlen = print(lengths[0])
maxlen = print(lengths[-1])
print(mean(lengths))
print(math.sqrt(stdev(lengths) / len(lengths)))
print(median(lengths))

