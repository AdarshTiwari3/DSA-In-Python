class CustomStack:

    def __init__(self, maxSize: int):
        self.max=maxSize
        self.stack=[]

    def push(self, x: int) -> None:
        if len(self.stack)<self.max:
            self.stack.append(x)
        return

    def pop(self) -> int:
        if len(self.stack)==0:
            return -1
        else:
            x=self.stack.pop()
            return x
        

    def increment(self, k: int, val: int) -> None:
        for i in range(len(self.stack)):
            if i<k:
                self.stack[i]+=val
                
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)