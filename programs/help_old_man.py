def solve(t,s,d,m,N,n,count):
    if N==1:
        count[0]+=1
        if count[0]==n:
            count.append((s,d))
            #return s,d
        return
    solve(t,s,m,d,N-1,n,count)
    count[0]+=1
    if count[0]==n:
        count.append((s,d))
        #return s,d
    solve(t,m,d,s,N-1,n,count)
    
    
    
    

t=int(input())
for i in range(t):
    N,n=input().split()
    N,n=int(N),int(n)
    
    count=[0]
    solve(i,1,3,2,N,n,count)
    print(count,n)
    print(count[1][0],count[1][1])