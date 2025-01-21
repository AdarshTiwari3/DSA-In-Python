# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=None
        cnt1=[0]
        def helper(root):
            nonlocal ans,k,cnt1
            if root is None:
                return 
            
            helper(root.left)
            cnt1[0]+=1
            if cnt1[0]==k:
                ans=root.val
                return
            
            helper(root.right)
            
        helper(root)
        return ans
        