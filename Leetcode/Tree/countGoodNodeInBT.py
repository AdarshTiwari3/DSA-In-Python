# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans=0
        def helper(root,mx):
            nonlocal ans
            if root is None:
                return
            mx=max(mx,root.val)
            # print("mx=",mx)
            if root and root.val>=mx:
                ans+=1
            
            
            helper(root.left,mx)
            helper(root.right,mx)
        helper(root,root.val)
        return ans