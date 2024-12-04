# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, p, q):
        if not p or not q:
            return p==q
        return p.val==q.val and self.helper(p.left,q.right) and self.helper(p.right,q.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left,root.right)
        