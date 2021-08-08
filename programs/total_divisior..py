def getTotalX(a, b):	
	divisor=[]
	mm=min(b)
	for i in range(1,mm+1):
		error='f'
		for j in a:
			if(i%j!=0):
				#print(i)
				error='t'
				break
		if(error=="f"):
			divisor.append(i)			
	print(divisor)			
	sec_div=[]
	for i in divisor:
		error="f"
		for j in b:
			if(j%i!=0):
				error="t"
				break
		if(error=="f"):
			sec_div.append(i)
	return (len(sec_div))
a=[2,6]
b=[12,16,18]
result=getTotalX(a,b)
print(result)
	