# Queue implementation using List
class Queue:
    def __init__(self):
        self.queue=[]

    def isEmpty(self):
        return self.queue==[] or len(self.queue)==0
    
    def enqeue(self,val):
        self.queue.append(val)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.queue.pop(0) # this will remove the value at 0th index
    
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.queue[0]
    
    def getFront(self):
        return self.peek()
    
    def getRear(self):
        return self.queue[-1]
    

q=Queue()
q.enqeue(10)
q.enqeue(20)
q.enqeue(30)
print(q.queue)
print(q.dequeue())
print(q.queue)
print(q.getFront())
print(q.getRear())
print("Is queue empty=",q.isEmpty())
print("size of queue=",len(q.queue))
    