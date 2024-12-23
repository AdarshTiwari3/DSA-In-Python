# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,targetSum):
        if root is None:
            return False
        if not root.left and not root.right and root.val==targetSum :
            return True
       
        return self.helper(root.left,targetSum-root.val) or self.helper(root.right,targetSum-root.val)
        
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.helper(root,targetSum)