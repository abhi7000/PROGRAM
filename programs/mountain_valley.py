def countingValleys(n, s):
	count=0
	x=0
	int_list=[]
	for i in s:
		if(i=='D'):
			x-=1
			int_list.append(x)
		elif(i=="U"):
			x+=1
			int_list.append(x)
	print(int_list)
	count=0
	for i in range(len(int_list)-1):
		temp=int_list[i]
		item=int_list[i+1]
		if(temp<0 and item==0):
			count+=1
	print(count)
	return count		
			
			
			
			
s="UUDDDDUUUDDU"
result=countingValleys(10,s)
		