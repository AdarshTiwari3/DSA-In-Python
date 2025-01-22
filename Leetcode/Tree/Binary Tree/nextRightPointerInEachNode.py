"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        q=deque()
        q.append(root)
        root.next=None
        while q:
            n=len(q)
            for i in range(n):
                node=q.popleft()
                if i < n-1: # it will always skip the last node as we have already last node is set to None
                    node.next=q[0]  # always points to the next node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root