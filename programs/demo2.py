n=int(input())
l=[0,1]
x=l[-1]+l[-2]
while(x<n):
	l.append(l[-1]+l[-2])
	x=l[-1]+l[-2]

for i in l:
	print(i,end=" ")
