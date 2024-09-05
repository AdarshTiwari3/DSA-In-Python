# Queue implementation using linked list
class Node:
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next

class Queue:
    def __init__(self, front=None, rear=None):
        self.front=front
        self.rear=rear

    def isEmpty(self):
        if self.front is None:
            return True
        return False

    def enqueue(self, val):
        if self.front is None:  #if the queue is empty then the front and rear will be the same node
            self.front=self.rear=Node(val)

        else: #if the queue is not empty then we will add the new node at the end of the queue
            self.rear.next=Node(val)
            self.rear=self.rear.next

    def dequeue(self):
        if self.front is None: #if the queue is empty then we can't delete any node
            print("Queue is empty")
            return
        else: #if the queue is not empty then we will delete the front node
            self.front=self.front.next  # move the head to the next node
            if self.front is None:
                self.rear=None
    
    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return
        else:
            return self.front.val
    def display(self):
        temp=self.front
        while temp:
            print(temp.val, end=' -> ')
            temp=temp.next
        print("None")

queue=Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
print("Queue is empty=",queue.isEmpty())
print("Peek={}".format(queue.peek()))
print("Rear={}".format(queue.rear.val))
queue.dequeue()
queue.display()

