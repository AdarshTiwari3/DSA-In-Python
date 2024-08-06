# Circular Doubly Linked List is a type of linked list in which each node apart from storing its data has two links. first link points to the previous node in the sequence and the second link points to the next node in the sequence. The last node of the linked list points to the first node of the linked list and the first node of the linked list points to the last node of the linked list. This forms a circular doubly linked list.

class Node: #node signature / Blueprint

    def __init__(self, prev=None, val=None, next=None):
        self.prev=prev
        self.val=val
        self.next=next

class CircularDoublyLinkedList:
     
    def __init__(self, head=None):
        # if head is not None:
        #     self.head=head
        #     self.head.prev=self.head
        #     self.head.next=self.head
        # else:
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
            while temp.next!= self.head: # if the next of the temp is head then it is the last node
                print(temp.val, end="->")
                temp = temp.next
            print(temp.val, end="->")
            print(temp.next.val) # this is just to display the head node in circular form
    
    # delete a node from the linked list at the beginning
    def delete_at_beginning(self):
        if self.is_empty():
            print("Linked list is empty")
            return
        # if we have only one node
        if self.head.next == self.head:
            self.head=None
        else: 

            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next

    # delete a node from the linked list at the end
    def delete_at_end(self):
        if self.is_empty():
            print("Linked list is empty")
            return
        # if we have only one node
        if self.head.next == self.head:
            self.head = None

        else:
            self.head.prev.prev.next=self.head
            self.head.prev = self.head.prev.prev

    # delete a node from the linked list at a specific position
    def delete_at_position(self , pos):
        if pos< 0 :
            print("Invalid position")
            return
        if pos == 0:
            self.delete_at_beginning()
            return
        
        if pos == 1:
            self.delete_at_end()
            return
        
        temp = self.head
        # traverse the linked list till the position-1 
        while pos > 1 and temp.next != self.head:
            temp = temp.next
            pos = pos - 1
        print(pos)
        if pos > 1: # check for out of bound
            print("Invalid position")
            return
        else :
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
    def search(self, val):
        temp = self.head
        if self.is_empty():
            print("The linked list is empty")
            return
        self.index = 0
        while temp.next != self.head:
            if temp.val == val:
                return self.index, True, temp
            temp = temp.next
            self.index = self.index + 1
        return None, False, None
    
    #iterator for the linked list
    def __iter__(self):
        return CircularDLLIterator(self.head)
    
class CircularDLLIterator:

    def __init__(self, head):
        self.current = head
        self.head = head
        self.count = 0
    def __iter__(self):
        return self
    
    def __next__(self):

        if self.current is None:
            raise StopIteration
        if self.current is self.head and self.count > 0:
            raise StopIteration
        else :
            self.count = self.count + 1
            val = self.current.val
            self.current = self.current.next
            return val
        

listNode=CircularDoublyLinkedList()
listNode.insert_at_beginning(10)
listNode.insert_at_end(20)
listNode.insert_at_end(30)
listNode.insert_at_beginning(2)
listNode.insert_at_position(15, 2)
listNode.insert_after_node(25, listNode.head.next.next)
listNode.display()
print("List after deleting the node-")
listNode.delete_at_end()
listNode.delete_at_beginning()
listNode.delete_at_position(4)
listNode.display()
index, found, node = listNode.search(15)
if found:
    print("The value is found at index", index)
else:    
    print("The value is not found in the linked list")

print("Circular Doubly Linked List using iterator=", end=' ')
for val in listNode:
    print(val, end='->')

print("\n")


    


 