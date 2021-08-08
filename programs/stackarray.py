def CreateStack():
	stack=[]
	print ("Stack Created")
	return stack
def IsEmpty(stack):
	if(len(stack)==0):
		return True
def Push(stack,element):
	stack.append(element)
	print(str(element)+"pushed")
def Pop(stack):
	if(IsEmpty(stack)):
		print ("stack Empty")
	else:
		temp=stack.pop()
		print(str(temp)+"popped")
def Peek(stack):
	print( str(stack[len(stack)-1]))
def ViewStack(stack):
	print (stack)

newStack=CreateStack()
ViewStack(newStack)
Pop(newStack)
Push(newStack,1)
Push(newStack,2)
Push(newStack,3)
ViewStack(newStack)
Push(newStack,4)
Push(newStack,5)
ViewStack(newStack)
Pop(newStack)
Pop(newStack)
Peek(newStack)
ViewStack(newStack)
