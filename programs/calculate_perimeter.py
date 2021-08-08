import math
arr=[[-3,9],[-8,7],[-12,4],
[-6,-2],[-4,-6],[2,-8],[6,-5],
[10,-3],[8,5],[4,8]]
total=0
longest=0
for i in range(len(arr)-1):
	distance=0
	x=arr[i][0]-arr[i+1][0]
	y=arr[i][1]-arr[i+1][1]
	rootvalue=(x**2)+(y**2)
	distance=math.sqrt(rootvalue)
	if(distance>longest):
		longest=distance
	total+=distance
print ("total= ",total)
print("average= ",total/len(arr))
print("longest= ",longest)
