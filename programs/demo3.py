n=30
x=0
def getsum(n):
	global x
	if(n<10):
		return n
	x=n%10
	n=n//10
	return x+getsum(n)
print(getsum(n))
