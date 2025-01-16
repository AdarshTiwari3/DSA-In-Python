# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        curr=root
        while curr:
            if p.val>curr.val and q.val>curr.val:
                # move right
                curr=curr.right
            elif p.val<curr.val and q.val<curr.val:
                # move left
                curr=curr.left
            else:
                # LCA found because they have opposite values
                return curr

        return None