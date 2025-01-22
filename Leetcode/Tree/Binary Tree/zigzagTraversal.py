# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=deque([root])
        flag=0
        ans=[]
        while q:
            n=len(q)
            local=[]
            # print('local=',local)
            
            for i in range(n):
                node=q.popleft()
                
                if node:
                    if flag==0:
                        local.append(node.val)
                    else:
                        local.insert(0,node.val) # every time insert at zero so it will be inserted as right to left direction
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            ans.append(local)
            flag=not flag
            
        return ans