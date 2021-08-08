def count(i,k):
	k+=1
	if(i==0):
		k+=1
		return k
	count(i-1,k)
	print(k)
	return k
count(4,9)
