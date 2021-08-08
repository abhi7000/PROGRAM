class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class CreateStack:
	def __init__(self):
		self.head=None
	def IsEmpty(self):
		if(self.head==None):
			return True
		else:
			return False
	def Push(self,element):
		if(self.head==None):
			new=Node(element)
			self.head=new
		else:
			new=Node(element)
			temp=self.head
			while(temp.next!=None):
				temp=temp.next
			temp.next=new
	def Pop(self):
		if(self.IsEmpty()):
			print ("Stack Empty")
		else:
			temp=self.head
			count=0
			while(temp.next!=None):
				temp=temp.next
				count+=1
			popitem=temp.data
			temp=self.head
			for i in range(count-1):
				temp=temp.next
			temp.next=None
			print(str(popitem)+" popped")
	def Peek(self):
		if(self.IsEmpty()):
			print ("Stack Empty")
		else:
			temp=self.head
			while(temp.next!=None):
				temp=temp.next
			print(temp.data)
	def ViewStack(self):
		temp=self.head
		print(" ")
		while(temp!=None):
			print (temp.data)
			temp=temp.next
			
		   
newStack=CreateStack()
newStack.ViewStack()		
newStack.Push(1)
newStack.Push(2)
newStack.Push(3)
newStack.Push(4)
newStack.Push(5)
newStack.Push(6)
newStack.ViewStack()
newStack.Pop()
newStack.ViewStack()
newStack.Peek()	
newStack.Pop()
newStack.ViewStack()