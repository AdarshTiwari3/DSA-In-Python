# Circular Doubly Linked List is a type of linked list in which each node apart from storing its data has two links. first link points to the previous node in the sequence and the second link points to the next node in the sequence. The last node of the linked list points to the first node of the linked list and the first node of the linked list points to the last node of the linked list. This forms a circular doubly linked list.

class Node: #node signature / Blueprint

    def __init__(self, prev=None, val=None, next=None):
        self.prev=prev
        self.val=val
        self.next=next

class CircularDoublyLinkedList:
     
    def __init__(self, head=None):
        if head is not None:
            self.head=head
            self.head.prev=self.head
            self.head.next=self.head
        else:
            self.head=head

    # check for empty linked list
    def is_empty(self):
        return self.head == None
    
    # insert a node at the beginning of the linked list

    def insert_at_beginning(self, val):
        node = Node(val=val) #create a new node with the value, in prev and next by default it is None

        if self.head is None:
            self.head = node
            self.head.prev=node # update the prev of head to the new node
            self.head.next=node 
        else :
            node.next=self.head
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head.prev = node
            self.head=node

    # insert a node at the end of the linked list
    def insert_at_end(self, val):
        node = Node(val = val)

        if self.is_empty():
            self.insert_at_beginning(val) #this will also update the head node
        else:
            node.prev = self.head.prev
            self.head.prev.next = node
            node.next = self.head
            self.head.prev = node

    # insert after a node

    def insert_after_node(self, val, prev_node):

        if self.is_empty():
            print("The linked list is empty")
            return
        else :
            temp = self.head
            while temp!=prev_node and temp.next != self.head: # temp.next is not head means we have reached the last node
                temp = temp.next
            if temp!= prev_node:
                print("The node is not present in the linked list")
                return
            else :
                node = Node(val=val)
                node.next = temp.next
                temp.next.prev = node
                node.prev = temp
                temp.next = node

    # insert at a specific position
    def insert_at_position(self, val, pos):
        if pos < 0:
            print("Invalid position")
            return
        if pos == 0:
            self.insert_at_beginning(val)
        else:
            node = Node(val=val)
            temp = self.head
            # traverse the linked list till the position-1
            while pos> 1 and temp.next !=self.head:
                temp = temp.next
                pos = pos - 1
            if pos>1:
                print("Invalid position")
                return
            node.next = temp.next
            node.prev = temp
            node.next.prev = node
            temp.next = node
    # display the linked list
    def display(self):
        if self.is_empty():
            print("The linked list is empty")
            return
        else: 
            temp = self.head
            while temp.next != self.head or self.head.prev!=temp: # if the next of the temp is head then it is the last node
                print(temp.val, end="->")
                temp = temp.next
            print(temp.val, end="->")
            print(temp.next.val) # this is just to display the head node in circular form
        

listNode=CircularDoublyLinkedList()
listNode.insert_at_beginning(10)
listNode.insert_at_end(20)
listNode.insert_at_end(30)
listNode.insert_at_beginning(2)
listNode.insert_at_position(15, 2)
listNode.insert_after_node(25, listNode.head.next.next)
listNode.display()


    


 