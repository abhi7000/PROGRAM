#User function Template for python3
def solve(arr,l,r,sumarr,sums):
	if(l>r):
		if sums not in sumarr:
			sumarr.append(sums)
		return 

	solve(arr,l+1,r,sumarr,sums+arr[l])
	solve(arr,l+1,r,sumarr,sums)
	return sumarr
    

def subsetSums(arr, N):
	# code here
	if(len(arr)>0):
	    l=0
	    r=N-1
	    sums=0
	    sumarr=[]
	    result=solve(arr,l,r,sumarr,sums)
	    result.sort()
	    return result
arr=[i for i in range(10)]
print(arr)    
res=subsetSums(arr, 10)
print(res)