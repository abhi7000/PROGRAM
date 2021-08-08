for i in range(1,6):
	for j in range(1,6):
		if(j<=6-i):
			print(6-i,end="")
		else:
			print(' ',end="")
	print()