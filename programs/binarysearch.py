

def binarysearch(arr,first,last,element):
	if(last>=first):
		
		mid=int((first+last)/2)
		if(arr[mid]==element):
			print("Element found at "+str(mid))
		elif(arr[mid]>element):
			return binarysearch(arr,first,mid-1,element)
		elif(arr[mid]<element):
			return binarysearch(arr,mid+1,last,element)
	else:
		print("Element not Found")


arr=[11,22,33,44,55,66,88]
binarysearch(arr,0,len(arr)-1,88)