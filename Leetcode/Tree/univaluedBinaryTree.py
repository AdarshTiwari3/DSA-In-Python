# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left:
            if root.val is not root.left.val:
                return False
        if root.right:
            if root.val is not root.right.val:
                return False
        left=self.isUnivalTree(root.left)
        
        right=self.isUnivalTree(root.right)
      
    
        return left and right