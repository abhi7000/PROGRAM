#code
def solve(n,start,mid,end,k):
    
    if(n==1):
        k-=1
        if(k==0):
            # print(n,k)
            print(start,end)
        return k
  
    k=solve(n-1,start,end,mid,k)
    k-=1
    if(k==0):
        # print(n,k)
        print(start,end)
    k=solve(n-1,mid,start,end,k)
    return k
 

test=int(input())
for i in range(test):
    n,k=input().split()
    start,mid,end=1,2,3
    # print("iiii=",i,n,k)
    solve(int(n),start,mid,end,int(k))