def birthday(s, d, m):
	count=0
	if(m>1 and (len(s)>=1) and m<=len(s)):
		for i in range(len(s)-(m-1)):
			curr=s[i]
			for j in range(1,m):
				print(i,end="")
				curr+=s[i+j]
			if(curr==d):
				print("added",i)
				count+=1
	else:
		if(s[0]==d):
			count+=1
	return count
	
s=[2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1]
result=birthday(s,18,7)
print (result)