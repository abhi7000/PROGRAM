def string_conversion(sentence):
	swap_word=[]
	for i in sentence:
		#print(i,end=" ")
		if(i.isupper()==True):
			swap_word.append(i.lower())
		elif(i.islower()==True):
			swap_word.append(i.upper())
		elif(i==" "):
			swap_word.append(" ")
		
	#print(swap_word)
	reverse=[]
	#for i in reversed(swap_word):
	#print(i,end="")
	reverse="".join(swap_word)
	#print(reverse)
	result=[]
	result=reverse.split()
	print(result)
	completed=[]
	for i in reversed(result):
		completed.append(i)
	last_output=" ".join(completed)
	return last_output
	#	return s
		
output=string_conversion("aWESOME is cODING")
print(output)