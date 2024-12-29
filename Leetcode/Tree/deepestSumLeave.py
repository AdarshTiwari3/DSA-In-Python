# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q=deque([root])
        summ=0
        while q:
            n=len(q)
            local_sum=0
            for i in range(n):
                node=q.popleft()
                local_sum+=node.val
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            # print("local_sum=",local_sum)
            summ=local_sum
        return summ