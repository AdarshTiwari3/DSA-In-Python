# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q=deque([(root,0)])
        ans=0
        while q:
            size=len(q)
            first_idx,last_idx=0,0
            for i in range(size):
                node,curr_idx=q.popleft()
                # if node:
                #  print("node-",node,"----->>>>id=",curr_idx)
                if i==0:
                    first_idx=curr_idx
                if i==size-1:
                    last_idx=curr_idx
                if node.left:
                    q.append((node.left,2*curr_idx+1))
                
                if node.right:
                    q.append((node.right,2*curr_idx+2))
            ans=max(ans,last_idx-first_idx+1)
        return ans

