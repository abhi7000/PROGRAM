#code
def longss(s):
    maxs=1
    max1s=1 
    for k in range(len(s)):
        ls=k
        fs=k
        
        for l in range(len(s)):
        
            try:
                if(s[k-l]==s[k+l]):
                    ls=k+l
                    fs=k-l
                else:
                    break
            except:
                break
        # print(ls,fs)
        if((ls-fs+1)>maxs):
            maxs=ls-fs+1
            
        ls=k
        fs=k   
        for l in range(len(s)):
        
            try:
                if(s[k-l]==s[k+l+1]):
                    ls=k+l+1
                    fs=k-l
                else:
                    break
            except:
                break
        if((ls-fs+1)>max1s):
            max1s=ls-fs+1
        # print(maxs,max1s)
    return max(maxs,max1s)
test=int(input())
for i in range(test):
    s=input()
    # print(longss(s))
    print(len(s)-longss(s))