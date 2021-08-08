
def maxMoves(s, t):
    # Write your code here
	popitem=[]
	slist=[]
	for i in s:
		slist.append(i)
		print(slist)
	for i in slist:	
		if(i==t):
			index=slist.index(i)
			slist.remove(index)
			print (slist)
	#return popitem
s="bcbbc"
t="b"
result=maxMoves(s,t)
#print (result)