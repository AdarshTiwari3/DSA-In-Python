#Singly Linked List implementation in Python- 
#singly linked list is a data structure that holds a sequence of elements in a linear order.

class Node: #node signature/ blueprint
    def __init__(self, val=None, next=None):
        self.val = val #value of the node
        self.next = next #pointer to the next node

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head  #head of the linked list

    #check for empty linked list
    def is_empty(self):
        return self.head == None #return True if the linked list is empty, otherwise False because head is None/emtpy
       
    #insert a node at the beginning of the linked list
    def insert_at_beginning(self, val):
        node=Node(val) #create a new node with the value
        # we can have two cases here, if the linked list is empty or have some nodes
        if self.is_empty(): # or we can put if self.head == None:
            self.head = node
        else: #if the linked list is not empty
            node.next=self.head
            self.head=node
        #another way to do this is to use the below code
        #node=Node(self, val, self.head) #create a new node with the value and point it to the head
        #self.head=node #update the head to the new node created
    
    #insert a node at the end of the linked list
    def insert_at_end(self, val):
        node=Node(val) # the default value of the next node is None
        # we can have two cases here, if the linked list is empty or have some nodes
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while (temp.next): #or we can put while temp.next != None:, temp.next is not None
                temp = temp.next # traverse the linked list till the end where the next node is None
            #update the link of the last node to the new node
            temp.next = node

    #insert a node at a specific position in the linked list
    def insert_at_position(self, val, position):
        if position < 0:
            print("Invalid position")
            return
        if position == 0: #if the position is 0, insert the node at the beginning
            self.insert_at_beginning(val)
        else:
            node = Node(val)
            temp = self.head
            while position > 1 and temp.next:
                temp = temp.next
                position = position - 1 #decrement the position, it goes to the next node till the position is 1
            if position > 1: # checks out of bound
                print("Invalid position")
                return
            node.next = temp.next
            temp.next = node
        
    # Search for a node in the linked list
    def search(self, val):
        temp = self.head
        self.index = 0
        while temp.next:
            if temp.val == val:
                return self.index, True, temp #return the index of the value in the linked list, and True if the value is found
            temp = temp.next
            self.index = self.index + 1
        return None #return -1 if the value is not found in the linked list
    
    #insert after a node in the linked list
    def insert_after_node(self, val, checkNode):
        if checkNode is not None:
            node= Node(val, checkNode.next) #connecting the link with the next of the given node, we will save some steps of code
            checkNode.next = node #update the link of the given node to the new node
        else:
            print("The given node is not found in the linked list")

    #delete a node from the linked list
    def delete(self, val):
        temp = self.head
        if temp.val == val: # if it is head node
            self.head = temp.next #update the head to the next node
            return
        else: 
            while temp.next:
                if temp.next.val == val:
                    temp.next = temp.next.next
                    return  #return if the value is found and deleted
                temp = temp.next
            print("The given node is not found in the linked list")

    #delete a node at a specific position in the linked list
    def delete_at_position(self, position):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.head = self.head.next #update the head to the next node
            return
        temp = self.head
        while position > 1 and temp.next:
            temp = temp.next
            position = position - 1 #reach the till the required position
        if position > 1:
            print("Invalid position")
            return
        temp.next = temp.next.next #update the link of the previous node to the next node of the next node    

    #display the linked list
    def display(self):
        temp = self.head
        while temp and temp.next:
            print(temp.val, end=' -> ')
            temp = temp.next #traverse the linked list till the end
        print("None")

        
#driver code
listNode = SinglyLinkedList()
listNode.insert_at_beginning(1)
listNode.insert_at_beginning(2)
listNode.insert_at_end(3)
listNode.insert_at_end(4)
listNode.insert_at_beginning(5)
listNode.insert_at_position(6, 0)
listNode.insert_at_position(7, 3)
listNode.insert_at_position(8, 8)
listNode.insert_after_node(9, listNode.head.next.next)
listNode.delete(5)
listNode.delete_at_position(2)
foundAt,isFound, value=listNode.search(7)
print("Linked list=",end = ' ')
listNode.display() 
print("The value is found at index ", foundAt) if isFound else print("The value is not found") 
print("The value is", value.val) if isFound else print("The value is not found")
# output: Invalid position
# Linked list= 6 -> 2 -> 7 -> 1 -> 3 -> None
# The value is found at index  2
# The value is 7
        
