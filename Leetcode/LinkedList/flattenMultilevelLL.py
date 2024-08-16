"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def helper(self, head):
        curr=head
        tail=head
        while curr:
            nextNode=curr.next
            childNode=curr.child
            if childNode:
                nhead=self.helper(childNode) #means last or tail node of the child
                print("nhead=",nhead.val)
                nhead.next=nextNode
                # print("nextNode-",nextNode.val)
                if nextNode:
                    nextNode.prev=nhead
                curr.next=childNode
                curr.child=None
                childNode.prev=curr
                
                curr=nhead
            else:
                if curr:
                    tail=curr
                    curr=nextNode   
        return tail
        
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.helper(head)
        return head
        