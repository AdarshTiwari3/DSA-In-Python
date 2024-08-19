# stack implementation using inherited list
class Stack(list): # inheriting list class
    def is_empty(self): # self is the list object, self=[]
        return self==[] or len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return super().pop() # this will create an infinite loop because pop() is the method of the list class and we are calling it here so it will call itself so it is overriden, so instead of calling self.pop() we are calling super().pop()
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self[-1]
    def display(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self
    def size(self):
        return len(self)
    def insert(self, index, value):
        raise AttributeError("Insert method is restricted in stack")
    
stk=Stack()
stk.push(1)
stk.push(2)
stk.push(3)
print("top element:",stk.peek())
print("stack:",stk.display())
print("pop element:",stk.pop())
print("stack:",stk.display())
print("stack is empty:",stk.is_empty())
print("size of stack:",stk.size())
# restrict the insert method in the stack class because list has default property of insert method
# stk.insert(1,2)
