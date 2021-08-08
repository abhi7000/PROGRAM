def bubblesort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-1):
			if (arr[j]>arr[j+1]):
				arr[j],arr[j+1]=arr[j+1],arr[j]
	for i in range(len(arr)-1):
		print (arr[i])


arr=[1258,644,9684,254,42,5965,4,50,50,70,5,5,567,78,77,98,900,9889,897,87878,76]
bubblesort(arr)