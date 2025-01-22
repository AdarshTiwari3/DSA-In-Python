# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue=deque([root])
        level=0
        ans=[-math.inf,0]
        print("ans=",ans[0])
        while queue:
            level+=1
            local_sum=0
            for i in range(len(queue)):
                node=queue.popleft()
                if node:
                    local_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if ans[0]<local_sum:
                ans[0]=local_sum
                ans[1]=level

        return ans[1]