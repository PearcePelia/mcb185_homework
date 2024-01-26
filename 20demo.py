# 20demo.py by Pearce Pelia done

import math

print('hello, again')# greeting 
print(1 + 1)
print(1-1)
print(2*2)
print(1/2)
print(5//2)
print(5%2)
print(5*(2+1))
print(math.ceil(5.59))
print(math.pow(5,5))

def inv(x):
	return -x
 
print(3, inv(3))

def areacircle(r):
	a = 3.14 * r**2
	return a 
	
print(areacircle(5))

a=2
b=2
if a == b:
	print('a equals b')
	
	
c = a == b
print(c)
print(type(c))

a=2
b=3
if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b')