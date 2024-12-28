# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.ans=0
        def helper(root,summ, isRoot):
            if root is None:
                return 
            summ-=root.val
            if summ==0:
                self.ans+=1
            
            helper(root.left,summ,False)
            helper(root.right,summ,False)
            
            if isRoot:
                helper(root.left,targetSum,True)
                helper(root.right,targetSum,True)


        helper(root,targetSum,True)
        return self.ans