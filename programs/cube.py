import math
n=int(input())
length=[]
mat_c=0
for i in range(n):
    length.append(list(map(str,input().split())))
for j in range(n):
    for k in range(n):
        if(length[j][k]=='D'):
            mat_c+=1
print(math.floor(math.sqrt(mat_c)))