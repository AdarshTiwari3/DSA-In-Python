# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
       
        def helper(root,val):
            if root is None:
                return
            if val == root.val:
                return root
            if val < root.val:
                return helper(root.left,val)
            elif val>root.val:
                return helper(root.right,val)
            
            

        return helper(root,val)