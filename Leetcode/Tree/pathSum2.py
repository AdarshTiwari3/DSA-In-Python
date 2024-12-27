# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        def helper(root,targetSum,local):
            if root is None:
                return 

            local.append(root.val)
            #if leaf and target==node
            if root and root.left is None and root.right is None and targetSum==root.val:
                ans.append(local[:]) # append a copy of local
                
            
                
            left=helper(root.left,targetSum-root.val,local)
            right=helper(root.right,targetSum-root.val,local)
            #backtrack and pop the recent value as it was not the matching sum
            local.pop()
            
            

        helper(root,targetSum,[])
        return ans
        