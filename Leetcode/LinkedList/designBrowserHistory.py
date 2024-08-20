class Node:
    def __init__(self,prev=None,val=None,next=None):
        self.prev=prev
        self.val=val
        self.next=next

class BrowserHistory:

    def __init__(self,homepage: str):
        node=Node(val=homepage)
        self.head=node
        self.curr=self.head
        

    def visit(self, url: str) -> None:
        node=Node(val=url)
        self.curr.next=node
        node.prev=self.curr
        self.curr=self.curr.next
        print("head=",self.curr.val)
    def back(self, steps: int) -> str:
        while steps:
            if self.curr.prev:
                self.curr=self.curr.prev
            else:
                break
            steps-=1
        return self.curr.val
    def forward(self, steps: int) -> str:
        self.curr
        while steps:
            if self.curr.next:
                self.curr=self.curr.next
            else: 
                return self.curr.val
            steps-=1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)