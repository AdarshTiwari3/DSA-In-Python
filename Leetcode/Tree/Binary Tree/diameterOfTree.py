# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,ans):
        if root is None:
            return 0

        left=self.helper(root.left,ans)
        right=self.helper(root.right,ans)
        ans[0]=max(ans[0],left+right)
        return 1+max(left,right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        self.helper(root,ans)
        return ans[0]