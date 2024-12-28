# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev=None
        def helper(root):
            if root is None:
                return 

            helper(root.right)
            helper(root.left)
            root.right=self.prev
            root.left=None
            self.prev=root
        helper(root)
        return root
        
        

        
