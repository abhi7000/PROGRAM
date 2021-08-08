class Solution:
    def printTillN(self, N):
    	#code here 
        if(N==1):
            print(N,end=" ")
            return 1 
        self.printTillN(N-1)
        print(N,end=" ")
obj=Solution()
obj.printTillN(1)