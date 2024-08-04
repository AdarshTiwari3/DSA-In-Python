# Circular linked list is a linear data structure, in which last node points the head node

class Node:
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next

class SinglyCircularLL:

    def __init__(self, head=None):
        self.head=head # head node of the linked list
        if self.head is not None:
            self.head.next=self.head # next of head node points to head node itself

    # If the linked list is empty
    def is_empty(self):
        return self.head is None

    # insert at beginning
    def insert_at_beginning(self , val):
        node = Node(val)
        if self.is_empty():
            self.head = node #point head to the new node and update the next of new node to head because it is circular
            self.head.next = self.head
        else:
            temp = self.head 
            # check the first node which is head node and update the next of new node to head
            while temp.next != self.head :
                temp = temp.next

            # now we have got the head node
            temp.next = node  # update the next of last node to new node
            node.next = self.head # update the next of new node to head
            self.head = node # update the head to new node

    # insert at end
    def insert_at_end (self, val):
        node = Node (val)
        if self.head is None:
            self.head = node #point head to the new node and update the next of new node to head because it is circular
            self.head.next = self.head
        else:
            temp = self.head
            # check for last node 
            while temp.next is not self.head:
                temp = temp.next

            temp.next = node
            node.next = self.head

    # insert at position
    def insert_at_position(self, val, pos):
        if pos == 0:
            self.insert_at_beginning(val)
        else:
            node = Node(val)
            temp = self.head
            for i in range(pos-1):
                temp = temp.next
            node.next = temp.next
            temp.next = node 

    #display the linked list
    def display(self):
        temp = self.head
        if self.is_empty():
            print("The linked list is empty")
            return
        while temp.next != self.head:
            print(temp.val, end="->")
            temp = temp.next
        print(temp.val,end='->') #print the last node
        print(temp.next.val)    #print the head node
    #search for a node in the linked list
    def search(self, val):
        temp = self.head
        self.index = 0
        while temp.next != self.head:
            if temp.val == val:
                return self.index, True, temp
            temp = temp.next
            self.index = self.index + 1
        return None, False, None
    #delete a node from the linked list at beginning
    def delete_at_beginning(self):
        if self.is_empty():
            print("The linked list is empty")
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
    #delete a node from the linked list at end
    def delete_at_end(self):
        if self.is_empty():
            print("The linked list is empty")
        if self.head.next == self.head: #if there is only one node
            self.head = None

        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            temp.next = self.head
    #delete a node from the linked list at a specific position
    def delete_at_position(self, position):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.delete_at_beginning()
        else:
            temp = self.head
            while position > 1 and temp.next != self.head:
                temp = temp.next
                position = position - 1
            if position > 1:
                print("Invalid position")
                return
            # check for only 1 node
            if temp.next == self.head:
                self.head = None
            else:
                temp.next = temp.next.next
            
        
    
        
listNode=SinglyCircularLL()
listNode.insert_at_beginning(10)
listNode.insert_at_beginning(20)
# print("Insert at beginning")
listNode.insert_at_end(30)
listNode.insert_at_end(40)
listNode.insert_at_position(50, 2)
listNode.insert_at_position(60, 0)
listNode.insert_at_position(70, 6)
listNode.delete_at_beginning()
listNode.delete_at_end()
listNode.delete_at_position(2)
print("Circular Linked List:")
listNode.display()




