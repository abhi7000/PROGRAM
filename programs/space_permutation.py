lst=[]
def spaceString(str,op="",x=1):

    # Code here
    # print(str)
    global lst
    if(x==1):
        lst=[]
    x=2
    if(str==""):
        lst.append(op)   
        return lst
    if(op==""):
        if(len(str)>1):
            op+=str[0]
            str=str[1:]
        else:
            lst.append(str)
            return lst
    op1=op
    op2=op
    if(len(str)>0):
        op1+=" {}".format(str[0])
        op2+=str[0]
        str=str[1:]
        spaceString(str,op2,x)
        spaceString(str,op1,x)
        
    else:
        str=""
        spaceString(str,op2,x)
        spaceString(str,op1,x)
    return lst
test=int(input())
for i in range(test):
    s=input()
    arr=spaceString(s)
    for i in arr:
        print(i,end=" ")
    print()

