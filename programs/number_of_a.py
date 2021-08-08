def repeatedString(s, n):
	if(len(s)==1 and s=='a'):
		return n
	if(len(s)==1 and s!='a'):
		return 0
	lista=""
	stng=""
	stng=s*n
	print(stng)
	lista=stng[0:n]
	print(lista)
	count=0
	for i in lista:
		if(i=='a'):
			count+=1
	return count
s="aba"
n=10000000
print(repeatedString(s,n))