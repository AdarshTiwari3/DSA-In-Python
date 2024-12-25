# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,depth,ans):
        if root is None:
            return
        if root and len(ans)<depth:
            ans.append(root.val)
        if root and root.val>ans[depth-1]:
            ans[depth-1]=root.val
        
        left=self.helper(root.left,depth+1,ans)
        right=self.helper(root.right,depth+1,ans)
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if root is None:
            return ans
        else:
            ans.append(root.val)
        self.helper(root,1,ans)
        return ans