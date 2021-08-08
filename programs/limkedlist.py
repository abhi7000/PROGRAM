
class Node:
	
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	
	def __init__(self):
		self.head=None
	
	def ViewNode(self):
		temp=self.head
		while(temp!=None):
			print(temp.data)
			temp=temp.next

	def InsertLastNode(self,data):
		NewNode=Node(data)
		temp=self.head
		while(temp.next!=None):
			temp=temp.next
		temp.next=NewNode

	def InsertFirstNode(self,data):
		newnode=Node(data)
		temp=self.head
		self.head=newnode
		self.head.next=temp
	def InsertMiddleNode(self,index,data):
		newnode=Node(data)
		temp=self.head
		while(temp.data!=index):
			temp=temp.next
		temp2=temp.next
		temp.next=newnode
		newnode.next=temp2

	def SortNode(self):
		temp=self.head
		while(temp.next!=None):
			
			nextnode=temp.next
			
			if(temp.data>nextnode.data):
				temp2=temp.data
				temp.data=nextnode.data
				nextnode.data=temp2
			temp=temp.next
				



first=LinkedList()
first.head=Node(1)
second=Node(2)
third=Node(3)
fouth=Node(4)
first.head.next=second
second.next=third
third.next=fouth 

first.InsertLastNode(9)

first.InsertFirstNode(10)
first.InsertMiddleNode(9,87)
first.SortNode()
first.ViewNode()
