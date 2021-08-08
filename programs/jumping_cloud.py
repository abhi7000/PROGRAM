def jumpingOnClouds(c,n):
	curr=0
	count=0
	end=1
	while(end!=0):
		print("entered",curr,count)
		try:
			if(c[curr+2]==0):
				count+=1
				curr+=2
				continue
           
		except:
			pass
		if(curr>=len(c)-1):
			end=0
			break
		if(c[curr+1]==0):
			curr+=1
			count+=1
		if(curr>=len(c)-1):
			end=0
			break
      
	return count

d="0 1 0 1 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 1 0 1 0 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 0 0 0 0 0 1 0 1 0 1 0 0 1 0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 0 0 0 1 0 0 1 0 1 0"
e=d.split()
f=map(int,e)
c=list(f)
n=7
#print((type(c[0])==int))
result=jumpingOnClouds(c,n)
print(result)
		