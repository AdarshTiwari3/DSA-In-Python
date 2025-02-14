# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        seen=set()
        def helper(root):
            if root is None:
                return False
            
            if helper(root.left):
                return True

            if k-root.val in seen:
                return True
            seen.add(root.val)
            return helper(root.right)

        return helper(root)