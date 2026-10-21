# DSA Practical Assignment 1 - Singly Linear Linked List (Simple)

class Node:
    def __init__(self, val):
        self.data = val     # value stored in node
        self.next = None    # reference to next node


class Linkedlist:
    def __init__(self):
        self.head = None    # first node (None = empty list)

    # Q1: Create linked list - append
    def create(self, new_node):
        if self.head is None:           # list empty: new node becomes head
            self.head = new_node
        else:
            temp = self.head
            while temp.next:            # go to last node
                temp = temp.next
            temp.next = new_node        # attach new node at the end

    # Q2: Traverse and print the node values
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("None")

    # Q3: Insert node at a specific position (1-based)
    def insert(self, new_node, pos):
        if pos == 1:                    # insert at beginning
            new_node.next = self.head
            self.head = new_node
        else:
            p = 1
            temp = self.head
            while p != pos - 1:         # move to (pos-1)th node
                temp = temp.next
                p += 1
            new_node.next = temp.next   # new node points to next node
            temp.next = new_node        # previous node points to new node

    # Q4: Delete the nodes having negative values
    def delete_negative(self):
        prev = None
        curr = self.head
        while curr:
            if curr.data < 0:               # negative node found
                if prev is None:            # it is the first node
                    self.head = curr.next
                else:                       # it is a middle / last node
                    prev.next = curr.next
            else:
                prev = curr                 # move prev only if no deletion
            curr = curr.next


# Q1: create list (positive numbers)
li = Linkedlist()
li.create(Node(10))
li.create(Node(20))
li.create(Node(30))
li.create(Node(40))
print("List Created")

# Q2: display
li.display()

# Q3: insert
print("Insert At pos 1")
li.insert(Node(50), 1)
li.display()

print("Insert At pos 3")
li.insert(Node(25), 3)
li.display()

# Q4: delete negative nodes (separate list with negative numbers)
neg = Linkedlist()
neg.create(Node(10))
neg.create(Node(-20))
neg.create(Node(30))
neg.create(Node(-40))
print("List with negative values")
neg.display()

print("After deleting negative nodes")
neg.delete_negative()
neg.display()