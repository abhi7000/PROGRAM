string="geeksforgeek"
strnew=[]
for i in string:
	string.
    if(len(string)-1!=i):
        if(string[i]!=last and string[i+1]!=string[i] ):
            strnew+=string[i]
            if(strnew[len(strnew)-1]==string[i]):
                print(strnew)
                strnew=strnew[:-1]
                print("deleted=",strnew)
        last=string[i]
    else:
        if(string[i]!=last):
            strnew+=string[i]

print(strnew)