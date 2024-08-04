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
            print("Invalid position")
            return
        if pos == 0:
            self.insert_at_beginning(val)
        else:
            node = Node(val)
            temp = self.last.next # start from the head node and traverse the linked list till pos-1
            while pos > 1 and temp.next is not self.last.next: # if last.next is head then it is the last node
                temp = temp.next
                pos = pos - 1 

            if pos > 1:
                print("Invalid position")
                return
            node.next = temp.next
            temp.next = node

    def display(self):
         
        if self.is_empty():
            print("The linked list is empty")
            return
        else:
            # means head node
            temp = self.last.next
            while temp != self.last:
                print(temp.val, end="->")
                temp = temp.next
            print(temp.val , end= '->') # print the last node because the loop will break before printing the last node
            # print the first node so that we could see list as a circular linked list
            print(temp.next.val) # this is just for display purpose although it is not required
        
    def search(self, val):
        temp = self.last.next
        index = 0
        while temp != self.last: #`last node is not checked because it is already checked in the loop
            if temp.val == val :
                return index, True, temp
            temp=temp.next
            index = index + 1
        # last node is remaining to check
        if temp.val == val:
            return index, True, temp
        return None, False, None
    
    def insert_after_node(self, val, checkNode):
        if checkNode is not None:
            node = Node(val, checkNode.next)
            checkNode.next = node
            if checkNode == self.last: # maintaining the last node
                self.last = node
        else:
            print("The given node is not found in the linked list")

    def delete_at_beginning(self):
        if self.is_empty():
            print("The linked list is empty")
            return
        if self.last.next == self.last: # if there is only one node in the linked list
            self.last = None
            return
        self.last.next = self.last.next.next
    def delete_at_end(self):
        if self.is_empty():
            print("The linked list is empty")
            return
        if self.last.next == self.last: # check for only one node in the linked list
            self.last = None
        else: 
            # traverse till last -1 node
            temp = self.last.next
            while temp.next is not self.last:
                temp = temp.next
            temp.next = self.last.next
            self.last = temp

    def delete_at_position(self, pos):

        if pos < 0:
            print("Invalid position")
            return
        if pos ==0 :
            self.delete_at_beginning()
            return
        if pos == 1:
            self.last.next.next = self.last.next
            return
        temp = self.last.next
        while pos > 1 and temp.next is not self.last.next:
            temp = temp.next
            pos = pos - 1
        if pos > 1:
            print("Invalid position")
            return
        temp.next = temp.next.next

    #iterating the linked list using iterator
    def __iter__(self):
        if self.is_empty():
            return None
        return circularSLLIterator(self.last.next)

class circularSLLIterator:
    def __init__(self, head):
        self.current=head
        self.head = head
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None: # if the current node is None then stop the iteration
            raise StopIteration
        if self.current == self.head and self.count > 0:
                raise StopIteration
        else:
            self.count = self.count + 1
            val = self.current.val
            self.current = self.current.next
            
            return val
        
        
    


circularSLL=SinglyCircularLL2()
circularSLL.insert_at_beginning(10)
circularSLL.insert_at_beginning(29)
circularSLL.insert_at_end(30)
circularSLL.insert_at_end(40)
circularSLL.insert_at_position(20,2)
circularSLL.insert_at_position(50,0)
circularSLL.insert_at_position(60,7)
circularSLL.insert_after_node(70, circularSLL.last)
index, found , node =circularSLL.search(30)
if found:
    print("The value is found at index ", index)
else:
    print("The value is not found")
circularSLL.delete_at_beginning()

circularSLL.delete_at_end()
circularSLL.delete_at_position(2)
circularSLL.display()

print("Circular Linked List using iterator=", end=' ')

for val in circularSLL:
    print(val, end='->')

