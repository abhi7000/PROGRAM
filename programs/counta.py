def repeatedString(s, n):
	count=0
	temp=0
	for i in s:
		if(i=='a'):
			temp+=1
	full=0
	full=int(n/len(s))
	count+=(temp*full)
	mod=0
	mod=n%len(s)
	strings=""
	string=s[0:mod]
	for i in string:
		if(i=='a'):
		count+=1
	return count
	
	