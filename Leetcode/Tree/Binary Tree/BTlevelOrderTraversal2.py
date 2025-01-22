# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if root is None:
            return ans
        q=deque()
        q.append(root)
        while q:
            n=len(q)
            local=[]
            for i in range(n):
                node=q.popleft()
                if node:
                    local.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            ans.insert(0,local) # this will insert from right to left everytime at index 0 remaing will shift one position
        return ans
        