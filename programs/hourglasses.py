def hourglassSum(arr):
    sums=[]
    maxs=0
    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            total=0
            total+=(arr[i][j]+arr[i][j+1]+arr[i][j+2])
            total+=(arr[i+1][j+1])
            total+=(arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            sums.append(total)
    maxs=max(sums)
    return maxs