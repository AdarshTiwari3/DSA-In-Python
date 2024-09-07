from collections import deque
class MyQueue:

    def __init__(self):
        self.st1=deque()
        self.st2=deque()

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        if len(self.st1):
            for i in range(len(self.st1)-1):
                self.st2.append(self.st1.pop())
            x=self.st1.pop()
            for i in range(len(self.st2)):
                self.st1.append(self.st2.pop())

        return x # return only left element from st1
        

    def peek(self) -> int:
        return self.st1[0]
        

    def empty(self) -> bool:
        return len(self.st1)==0 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

