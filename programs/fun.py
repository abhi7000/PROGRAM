import math as m
from fractions import Fraction
def fact(x):
    factorial = 1
    if int(x) >= 1:
        for i in range(1, int(x) + 1):
            factorial = factorial * i
    return factorial
def f(p,q,r):
    ans=0
    for i in range(p+1):
        temp = 0
        for j in range(1,q+1):
            ta = m.pow(r,i)
            tb = (ta-1)/ta
            temp += m.pow(tb,j)
        temp2 = fact(p)/(fact(p-i)*fact(i))
        if(i&1):
            ans-=temp*temp2
        else:
            ans+=temp*temp2
    print(ans)
    return ans
test=int(input())
for i in range(test):
    print("entered")
    p,q,r=map(int,input().split())
    print(p,q,r)
    ans=f(p,q,r)
    ans1=Fraction(ans)
    print(ans1)


