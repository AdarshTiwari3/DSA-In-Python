# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        summ=0
        def helper(root):
            nonlocal summ
            if root is None:
                return root
        #move from right root left i.e reverse inorder as it looks same in given testcase
            helper(root.right)
            summ+=root.val
            root.val=summ # put the sum value as a greater key
            helper(root.left)

            return root
        return helper(root)