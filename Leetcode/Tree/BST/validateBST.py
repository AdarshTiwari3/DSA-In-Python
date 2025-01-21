# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root,lb,ub):
            if root is None:
                return True
            if lb<root.val<ub:
                left=helper(root.left,lb,root.val)
                right=helper(root.right,root.val,ub)
                return left and right # if both side is true then only a valid BST
                
            return False

        return helper(root,-math.inf,math.inf)