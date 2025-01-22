# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left=self.minDepth(root.left)
        right=self.minDepth(root.right)

        return (min(left,right) if min(left,right) else max(left,right))+1