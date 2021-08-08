class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def inorder(root):
	temp=root
	if(temp):
		inorder(temp.left)
		print(temp.data,end=" ")
		inorder(temp.right)
def preorder(root):
	temp=root
	if(not temp):
		print("Tree Empty")
	else:
		print(temp.data,end=" ")
		preorder(temp.left)
		preorder(temp.right)
def postorder(root):
	temp=root
	if(not temp):
		print("Tree Empty")
	else:
		postorder(temp.left)
		postorder(temp.right)
		print(temp.data,end=" ")
def insertItem(root,key):
	newNode=Node(key)
	temp=root
	if(not temp):
		temp=newNode
	else:
		while(temp):
			if(not temp.left):
				temp.left=newNode
			elif(not temp.right):
				temp.right=newNode
			else:
				temp=temp.left

newTree=Node(1)
newTree.left=Node(2)
newTree.right=Node(3)
newTree.left.left=Node(4)
newTree.right.left=Node(5)
inorder(newTree)
insertItem(newTree,6)

			
	
	
	
	
	
	
	