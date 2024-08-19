# stack implementation using list   
class Stack:
    def __init__(self):
        self.stack=[]
    def is_empty(self):
        return self.stack==[] or len(self.stack)==0
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        # check if stack is empty
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return -1
        return self.stack[-1] # return the top element, -1 is the index of the top element which is the last element
    def display(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack
    def size(self):
        return len(self.stack)

stk=Stack()
print("stack is empty:",stk.is_empty())
stk.push(1)
stk.push(2)
stk.push(3)
stackk=stk.display()
print("top element:",stk.peek())
print("stack:",stackk)
print("pop element:",stk.pop())
print("stack:",stk.display())