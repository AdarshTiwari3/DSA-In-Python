# circular linked list using different methods

class Node:
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next

class SinglyCircularLL2:

    def __init__(self, last=None): # this time we will use last node instead of head node
        self.last=last

    def is_empty(self):
        return self.last is None
    
    def insert_at_beginning(self, val):
        node = Node(val)

        if self.is_empty():
            self.last = node 
            self.last.next = self.last

        else:
             node.next = self.last.next
             self.last.next = node

    def insert_at_end(self, val):
        node = Node(val)

        if self.last is None:
            self.last = node
            self.last.next = self.last
        else:
            node.next = self.last.next
            self.last.next = node
            self.last = node # update the last node to the new node

    def insert_at_position(self , val , pos):
        if pos < 0 :
            return 'Invalid position'
        if pos == 0:
            self.insert_at_beginning(val)
        else:
            node = Node(val)
            temp = self.last.next # start from the head node and traverse the linked list till pos-1
            while pos > 1 and temp.next is not self.last.next: # if last.next is head then it is the last node
                temp = temp.next
                pos = pos - 1 

            if pos > 1:
                return 'Invalid position'
            node.next = temp.next
            temp.next = node

    def display(self):
        temp = self.last.next # means head node
        if self.is_empty():
            print("The linked list is empty")
            return
        while temp != self.last:
            print(temp.val, end="->")
            temp = temp.next
        print(temp.val , end= '->') # print the last node because the loop will break before printing the last node
        # print the first node so that we could see list as a circular linked list
        print(temp.next.val) # this is just for display purpose although it is not required



circularSLL=SinglyCircularLL2()
circularSLL.insert_at_beginning(10)
circularSLL.insert_at_beginning(29)
circularSLL.display()