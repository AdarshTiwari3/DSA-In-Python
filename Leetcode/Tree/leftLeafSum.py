# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if root is None:
                return 0
            summ=0
            if root.left and root.left.left is None and root.left.right is None:
                summ=root.left.val
            
            return summ + helper(root.left) + helper(root.right)

        
        return helper(root)
    

#Solution 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.summ=0
        def helper(root):
            if root is None:
                return 0
            if root.left and root.left.left is None and root.left.right is None:
                self.summ+=root.left.val
            helper(root.left)
            helper(root.right)



        helper(root)
        return self.summ