# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        if root is None:
            return 0
        def helper(root,prev):
            if root is None:
                return 0

            left=helper(root.left,root.val)
            right=helper(root.right,root.val)

            self.ans=max(self.ans,left+right)
            print("ans=",self.ans,"left=",left,"right=",right)
            if root.val==prev:
                return 1+max(left,right)
            
            return 0
        helper(root,root.val)
        return self.ans