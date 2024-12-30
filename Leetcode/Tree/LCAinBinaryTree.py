# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root==p or root ==q:
            return root

        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)

        # check for left and right if it found then return the node else return none if left and right both have some value, mean you have got the lowest ancestor, means both have any same parent

        if left is None: 
            return right # if left is none then we need to return right

        elif right is None:
            return left
        else: # both matching 
            return root
        