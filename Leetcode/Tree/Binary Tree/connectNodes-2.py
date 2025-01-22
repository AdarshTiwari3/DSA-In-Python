"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        prev=temp=Node(-1)
        curr=root
        while curr:
            prev.next=curr.left
            if prev.next:
                prev=prev.next
            
            prev.next=curr.right

            if prev.next:
                prev=prev.next
            
            curr=curr.next
            if curr is None:
                prev=temp # as this stores the value of curr.left node in the starting
                curr=temp.next

        return root
#in O(1) space