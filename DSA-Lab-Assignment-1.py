#Node Structure
class Node:
	def __init__(self,value):
		self.data=value
		self.next=None


class LinkedList:
	def __init__(self):
		self.head=None 

	#Adding Node to Linkeddlist
	def Create(self,new_node):
		if self.head==None:
			self.head=new_node
		else:
			temp=self.head
			while(temp.next):
				temp=temp.next
			temp.next=new_node

	#inserting new node at given position
	def insert(self,new_node,pos):
		if pos==1:
			new_node.next=self.head 
			self.head=new_node
		else:
			p=1
			temp=self.head
			while(p!=pos-1):
				temp=temp.next
				p+=1 
			new_node.next=temp.next
			temp.next=new_node 


	#Findind middle node in Linkedlist
	def middle(self):
		c=0
		temp=self.head
		while(temp):
			c+=1
			temp=temp.next
		mid=c//2
		temp=self.head
		for i in range(0,mid):
			temp=temp.next
		print("Middle Value:",temp.data)


	#Deleting Node at given position
	def delete(self,pos):
		if pos==1:
			temp=self.head
			self.head=temp.next
		else:
			p=1
			temp=self.head
			while(p!=pos-1):
				temp=temp.next
				p+=1
			temp.next=temp.next.next
			 

	#Traverse and display each node
	def display(self):
		if self.head==None:
			print("Linked List Is Empty")
		else:
			temp=self.head
			while(temp):
				print(temp.data,end="->")
				temp=temp.next
			print("None")

	#Reverse Linkedlist
	def reverse(self):
		arr=[]
		temp=self.head
		while(temp):
			arr.append(temp.data)
			temp=temp.next
		temp=self.head

		for i in range(len(arr)-1,-1,-1):
			temp.data=arr[i]
			temp=temp.next

	#Addition of two consecutive nodes
	def add(self):
		if self.head==None:
			print("Linked List Is Empty")
		else:
			temp=self.head
			while(temp.next):
				sum=temp.data+(temp.next.data)
				print("Sum:",sum)
				temp=temp.next



li1=LinkedList()
li1.Create(Node(10))
li1.Create(Node(20))
li1.Create(Node(30))
li1.Create(Node(40))
li1.display()

li1.insert(Node(90),3)	#insertion at position 3
li1.insert(Node(50),5)	#insertion at position 5
li1.display()

li1.display()
li1.middle()	# display middle node value

li1.delete(3)	#deletion at position 3
li1.delete(1)	#deletion of head node
li1.display()

li1.add()	#Adding consecutive nodes
li1.display()

li1.reverse()	#Reverse list
li1.display()