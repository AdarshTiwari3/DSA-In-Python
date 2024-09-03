class MinStack:

    def __init__(self):
        self.stack=[]
        self.minimum=[]
    

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum:
            self.minimum.append(min(val,self.minimum[-1]))
        else:
            self.minimum.append(val)
    
        

    def pop(self) -> None:
        if len(self.stack)>0:
            self.stack.pop()
            self.minimum.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
obj.pop()
print(obj.getMin())
obj.pop()
