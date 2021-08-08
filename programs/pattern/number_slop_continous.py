pin=0
dig=0
for i in range(1,8):
	cpy=dig
	for j in range(0,i):
		if(j<=pin and (i%2!=0 or i==1)):
			print(pin+cpy-j+1,end=" ")
			dig+=1	
		else:
			print(' ',end="")
	if(i%2!=0):
		pin+=1		
	print()