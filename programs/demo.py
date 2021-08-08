strin=input()
string=list(strin)
# print(string)

def removeslice(string):
	global error
	for i in range(len(string)-1):
		start=-1
		end=-1
		for j in range(i+1,len(string)):

			# print("i="+string[i],i,"j="+string[j],j)
			if(string[i]==string[j]):
				start=i
				end=j
			else:
				break
		if(start!=-1):
			# print(start,end)
			del string[start:end+1]
			# print(string)
			error=True

			
		# print("last",string,error)
	

error=True



while(error):
	error=False
	removeslice(string)
	# print(error)
print("".join(string))

	