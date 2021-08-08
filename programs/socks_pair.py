def sockMerchant(n, ar):
	unique_list=[]
	dic={}
	for i in ar:
		if i not in unique_list:
			unique_list.append(i)
	for j in unique_list:
		dic[j]=None
	print (dic)	
	for item in unique_list:
		temp=item
		count=0
		for item1 in ar:
			if(item1==temp):
				count+=1
				dic[item]=count
	pairs=0
	print(dic)
	for dicitem in dic:
		if(dic[dicitem]>=2):
			pairs+=int(dic[dicitem]/2)
	return pairs
arr=[3,4,3,6,7,7,7,6]
result=sockMerchant(8,arr)
print(result)
