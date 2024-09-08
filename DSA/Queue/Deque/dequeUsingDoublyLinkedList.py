# deque implementation using doubly linked list- why doubly linked list?- because we need to access the previous node of the rear node, to avoid traversing the whole list to reach the previous node of the rear node.

class Node:
    def __init__(self, prev=None, val=None, next=None):
        self.prev=prev
        self.val=val
        self.next=next
    
class Deque: # deque is used to implement both stack and queue, here we can insert and delete elements from both the ends
    def __init__(self, front=None, rear=None, size=0):
        self.front=front
        self.rear=rear
        self.size=size

    def isEmpty(self):
        return self.front == None
    
    def insertFront(self, val):
        if self.isEmpty():
            self.front=self.rear=Node(val=val) # if the deque is empty then the front and rear will be the same node
        else:
            node=Node(val=val)
            # means the deque is not empty
            node.next=self.front
            self.front.prev=node
            self.front=node
        self.size+=1
    
    def insertRear(self, val):
        if self.front is None:
            self.front=self.rear=Node(val=val)
        else:
            node = Node(val=val)
            node.prev=self.rear
            self.rear.next=node
            self.rear=node
        self.size+=1

    def deleteFront(self):
        if self.isEmpty():
            print("deque is empty")
            return 
        else:
            self.front=self.front.next 
            #check if the queue is empty after deleting the front node
            if self.front is None:
                self.rear=None
            else:
                # break the prev link of the new front node
                self.front.prev=None
        self.size-=1

    def deleteRear(self):
        if self.isEmpty():
            print("deque is empty, can't delete")
            return 
        else:
            #move the rear to its previous node
            self.rear=self.rear.prev
            #check if the queue is empty after deleting the rear node
            if self.rear is None:
                self.front=None # suppose we have only element to delete
            else:
                #break the next link of the new rear node
                self.rear.next=None
        self.size-=1
    
    def getFront(self):
        if self.isEmpty():
            print("deque is empty")
            return 
        return self.front.val
    
    def getRear(self):
        if self.isEmpty():
            print("deque is empty")
            return 
        return self.rear.val
    
    def getSize(self):
        return self.size
    
    def display(self):
        if self.isEmpty():
            print("deque is empty, can't print anything")
            return
        temp=self.front
        while temp:
            print(temp.val, end=' -> ')
            temp=temp.next
        print("None")

deque=Deque()
deque.insertFront(20)
deque.insertFront(10)
deque.insertRear(30)
deque.insertRear(40)
deque.insertFront(2)
deque.display()
print("Front={}".format(deque.getFront()))
print("Rear={}".format(deque.getRear()))
deque.deleteFront()
deque.display()
deque.deleteRear()
deque.display()
print("Size={}".format(deque.getSize()))
print("Is empty={}".format(deque.isEmpty()))

