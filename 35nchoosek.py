# 35nchoosek.py by Pearce pElia 

def Ffunction(n):
	if n == 0 or n == 1:
		return 1 
	else:
		return n * Ffunction(n - 1)
	
def solve(n, k):
	if k < 0 or k > n:
		return 0
	else:
		return Ffunction(n) // (Ffunction(k) * Ffunction(n - k))
		
print(solve(11, 2))
print(solve(31, 4))
print(solve(51, 6))	