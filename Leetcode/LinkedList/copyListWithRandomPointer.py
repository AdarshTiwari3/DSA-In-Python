"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        while curr:
            copyNode=Node(curr.val)
            nextNode=curr.next
            curr.next=copyNode
            copyNode.next=nextNode
            curr=nextNode
        # print("head",head.next.val)
        curr=head
        
        while curr:
            print("curr1=",curr.val)
            fast=curr.next.next
            if curr.random:
                curr.next.random=curr.random.next
            curr=fast
        
        curr=head
        ans=Node(0)
        final_ans=ans
        while curr:
            print("curr",curr.val)
            fast=curr.next.next
            ans.next=curr.next
            ans=ans.next
            curr.next=fast
            curr=fast
        return final_ans.next