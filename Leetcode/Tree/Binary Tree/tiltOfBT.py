# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans=0
        def helper(root):
            nonlocal ans
            if root is None:
                return 0
            left=helper(root.left)
            right=helper(root.right)
            ans+=abs(left-right)

            return left+root.val+right

        helper(root)
        return ans
        