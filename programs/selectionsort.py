def selectionsort(arr):
	
	for i in range(len(arr)):
		min_index=i
		for j in range(i+1,len(arr)):
			if (arr[min_index]>arr[j]):
				min_index=j
		arr[i],arr[min_index]=arr[min_index],arr[i]
	for i in range(len(arr)):
		print(arr[i])

arr=[1,2,3,6,5,78989,5461,9741,9,64123 ,78,45,57,74]
selectionsort(arr)