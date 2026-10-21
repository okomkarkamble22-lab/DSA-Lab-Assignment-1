#Node Structure
class Node:
	def __init__(self,value):
		self.data=value
		self.next=None


class LinkedList:
	def __init__(self):
		self.head=None 

	#Q1. Create Linked List
	#Adding Node to Linkeddlist
	def Create(self,new_node):
		#If LL is empty, the new node becomes the first node (head)
		if self.head==None:
			self.head=new_node
		else:
			temp=self.head
			#Moving temp to the last node, because new node is added at the end
			while(temp.next):
				temp=temp.next
			#Linking the last node to the new node
			temp.next=new_node

	#Q3. Insert node at a specific position
	#inserting new node at given position
	def insert(self,new_node,pos):
		#If position is 1, new node points to old head and becomes the new head
		if pos==1:
			new_node.next=self.head 
			self.head=new_node
		else:
			p=1
			temp=self.head
			#Moving temp to the node before the given position (pos-1)
			while(p!=pos-1):
				temp=temp.next
				p+=1 
			#First linking new node to the next node, then previous node to new node, so the list does not break
			new_node.next=temp.next
			temp.next=new_node 


	#Q4. Find Middle node and print its value
	#Findind middle node in Linkedlist
	def middle(self):
		#Counting total number of nodes in LL
		c=0
		temp=self.head
		while(temp):
			c+=1
			temp=temp.next
		#Middle position is total//2 (for even count it gives the second middle node)
		mid=c//2
		#Moving mid steps from head to reach the middle node
		temp=self.head
		for i in range(0,mid):
			temp=temp.next
		print("Middle Value:",temp.data)


	#Q5. Delete node
	#Deleting Node at given position
	def delete(self,pos):
		#If position is 1, moving head to the second node so first node is removed
		if pos==1:
			temp=self.head
			self.head=temp.next
		else:
			p=1
			temp=self.head
			#Moving temp to the node before the node to be deleted
			while(p!=pos-1):
				temp=temp.next
				p+=1
			#Skipping the next node so it gets removed from LL
			temp.next=temp.next.next
			 

	#Q2. Traverse and print the node values
	#Traverse and display each node
	def display(self):
		#Checking if LL is empty
		if self.head==None:
			print("Linked List Is Empty")
		else:
			temp=self.head
			#Visiting every node from head till the end and printing its value
			while(temp):
				print(temp.data,end="->")
				temp=temp.next
			print("None")

	#Q6. Reverse list
	#Reverse Linkedlist
	def reverse(self):
		#Storing all node values in an array
		arr=[]
		temp=self.head
		while(temp):
			arr.append(temp.data)
			temp=temp.next
		temp=self.head

		#Writing values back from last to first, so the LL gets reversed
		for i in range(len(arr)-1,-1,-1):
			temp.data=arr[i]
			temp=temp.next

	#Q7. Calculate the sum of every two consecutive node values
	#Addition of two consecutive nodes
	def add(self):
		#Checking if LL is empty
		if self.head==None:
			print("Linked List Is Empty")
		else:
			temp=self.head
			#Adding current node value and next node value, then moving one node ahead
			while(temp.next):
				sum=temp.data+(temp.next.data)
				print("Sum:",sum)
				temp=temp.next



li1=LinkedList()
li1.Create(Node(10))	#Q1
li1.Create(Node(20))	#Q1
li1.Create(Node(30))	#Q1
li1.Create(Node(40))	#Q1
li1.display()	#Q2

li1.insert(Node(90),3)	#insertion at position 3 (Q3)
li1.insert(Node(50),5)	#insertion at position 5 (Q3)
li1.display()	#Q2

li1.display()
li1.middle()	# display middle node value (Q4)

li1.delete(3)	#deletion at position 3 (Q5)
li1.delete(1)	#deletion of head node (Q5)
li1.display()

li1.add()	#Adding consecutive nodes (Q7)
li1.display()

li1.reverse()	#Reverse list (Q6)
li1.display()