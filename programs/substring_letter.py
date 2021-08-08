
def buildSubsequences(s):
    # Write your code here
	letters=[]
	for i in s:
		if i not in letters:
			letters.append(i)
	letters.sort()
	words=[]
	n=0
	for i in range(len(s)):
		n+=1
		words.append(letters[i])
		while(n<len(s)):
			for j in range(i+1,len(s)):
				words.append(str("".join(letters[0:n+1]))+str(letters[j]))
			n+=1
	
	#return letters
	return words
s="acb"
result=buildSubsequences(s)
print(result)