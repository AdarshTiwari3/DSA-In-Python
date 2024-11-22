#Deque using list
class Deque:
    def __init__(self):
        self.deque=[]

    def isEmpty(self):
        return len(self.deque)==0 or self.deque==[]
    
    def insertFront(self, val):
        self.deque.insert(0, val)

    def insertRear(self, val):
        self.deque.append(val)

    def deleteFront(self):
        #check if the deque is empty
        if self.isEmpty():
            print("deque is empty")
            return
        else:
            self.deque.pop(0)

    def deleteRear(self):
        if self.deque==[]:
            print("deque is empty")
            return
        else:
            self.deque.pop()

    def getFront(self):
        if self.isEmpty():
            print("deque is empty")
            return
        else:
            return self.deque[0]
        
    def getRear(self):
        if self.isEmpty():
            print("deque is empty")
            return
        else:
            return self.deque[-1]
        
    def display(self):
        if self.isEmpty():
            print("deque is empty")
            return
        else:
            print(self.deque)

deque=Deque()
deque.insertFront(10)
deque.insertFront(20)
deque.insertRear(30)
deque.display() #[20, 10, 30]
deque.deleteFront()
deque.deleteRear()
deque.display() #[10]
print(deque.isEmpty()) #False