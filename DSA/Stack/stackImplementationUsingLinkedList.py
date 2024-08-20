# stack implementation using linked list
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    
class Stack:
    def __init__(self):
        self.head=None
        self.size=0
    
    def is_empty(self):
        return self.size==0 or self.head is None
    
    def push(self, val):
        node=Node(val)
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
        self.size+=1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            val=self.head.val
            self.head=self.head.next
            self.size=self.size-1
            return val
    def peek(self):
        if self.is_empty():
            return -1
        return self.head.val
    def display(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            temp=self.head
            while temp:
                print(temp.val,end='->')
                temp=temp.next
            print("None")
    def length(self):
        print("size=",self.size)
        return self.size

stk=Stack()
print("stack is empty:",stk.is_empty())
stk.push(1)
stk.display()
stk.push(2)
stk.display()
stk.push(3)
stk.push(4)
stk.display()
print("top element:",stk.peek())
print("pop element:",stk.pop())
stk.display()
print("size of stack:",stk.length())