#Doubly Linked List is a type of linked list in which each node apart from storing its data has two links. first link points to the previous node in the sequence and the second link points to the next node in the sequence.

class Node: #node signature / Blueprint

    def __init__(self, prev=None, val=None, next=None):
        self.prev=prev
        self.val=val
        self.next=next
       

class DoublyLinkedList:

    #initialize the head of the linked list
    def __init__(self, head=None):
        self.head=head

    #check for empty linked list
    def is_empty(self):
        return self.head == None 
    
    #insert a node at the beginning of the linked list
    def insert_at_beginning(self, val):
        node = Node(val=val) #create a new node with the value, in prev and next by default it is None

        if self.head is None:
            self.head = node
        else :
            node.next=self.head
            self.head.prev=node
            self.head=node

    #insert a node at the end of the linked list

    def insert_at_end(self, val):
        node = Node(val=val)

        if self.head == None:
            self.head = node
        
        else:
            temp = self.head
            while temp.next is not None: #traverse the linked list till the end where the next node is None
                temp = temp.next
            
            temp.next = node #update the link of the last node to the new node
            node.prev = temp # update the link of the new node to the last node

    #insert a node at a specific position in the linked list

    def insert_at_position( self, val, pos):
        node = Node(val=val)
        # check for head is None

        if pos==0:
            self.insert_at_beginning(val) # alternate way to insert at the beginning- self.head=node
            return 
        if pos < 0:
            print("Invalid position")
            return
        if pos > 1:
            temp = self.head
            # reach till that postion

            while pos > 1 and temp.next is not None:
                temp = temp.next 
                pos = pos - 1
            if pos > 1: # checks out of bound
                print("Invalid position")
                return
            
            # update the links
            node.next = temp.next
            node.prev = temp
            temp.next = node
            temp.next.prev = node

    # display the linked list
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end='-->')
            temp = temp.next
        print("None")
    
    # Search for a node in the linked list

    def search (self, val):
        temp = self.head
        index=0
        while temp:
            # checks if the value is found
            if temp.val == val:
                return index, True, temp
            temp = temp.next
            index=index+1
        return None, False, None

    #insert after a node in the linked list

    def insert_after_node(self, val, checkNode):
        node = Node(val=val)
        if checkNode:
            node.next = checkNode.next
            checkNode.next = node
            node.prev = checkNode
            if node.next:
                node.next.prev = node
        else:
            print("The given node is not found in the linked list")

    # delete at beginning of the linked list
    def delete_at_begining( self):
        if self.head is None: # check for empty linked list
            print("The linked list is empty")
            return
        else : # update the head to the next node
            self.head = self.head.next  # update the head to the next node
            self.head.prev = None # update the previous link of the new head to None

    # delete at end of the linked list
    def delete_at_end(self):
        # check for empty linked list
        if self.is_empty():
            print("The linked list is empty")
            return
        else: 
            #traverse till the end of the linked list
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next=None #update the link of the second last node to None
        
    # delete a node from the linked list at a specific position
    def delete_at_position(self, pos):
        if self.is_empty(): # check for empty linked list
            print("The linked list is empty")
            return
        else :
            if pos == 0 : # delete at the beginning
                self.delete_at_begining()
                return
            if pos < 0:
                print("Invalid position")
                return
            temp = self.head 
            # traverse till the position
            while pos > 0 and temp.next :
                temp = temp.next
                pos = pos - 1

            if pos > 0: # checks out of bound
                print("Invalid position")
                return
            # update the links
            temp.prev.next = temp.next # update the link of the previous node to the next node
            temp.next.prev = temp.prev # update the link of the next node to the previous node






DLL=DoublyLinkedList()
DLL.insert_at_beginning(10)
DLL.insert_at_beginning(20)
DLL.insert_at_end(30)
DLL.insert_at_end(40)
DLL.insert_at_position(25, 0)
DLL.insert_at_position(35, 4)
DLL.insert_after_node(45, DLL.head.next.next.next.next)
DLL.delete_at_begining()
DLL.delete_at_end()
DLL.delete_at_end()
DLL.delete_at_position(2)
index, found, node  =DLL.search(30)
print("Doubly Linked List= ", end='')
DLL.display()

if found:
    print("The value is found at index: {} and node: {}".format(index, node.val))
else:
    print("The value is not found in the linked list")

# Output:
# Doubly Linked List= 20-->10-->35-->None
# The value is not found in the linked list
