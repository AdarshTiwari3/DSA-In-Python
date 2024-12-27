# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0
        def helper(root,subString):
            nonlocal ans
            if root is None:
                return

            subString+=str(root.val)
            #if leaf
            if root and root.left is None and root.right is None:
                # convert the substring to int and add to the ans
                ans+=int(subString)
                subString=0
            
            helper(root.left,subString)
            helper(root.right,subString)

        helper(root,"")
        return ans
        

#Solution 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(root,summ):
            if root is None:
                return 0

            summ=summ*10+root.val
            #if leaf
            if root and root.left is None and root.right is None:
                # convert the substring to int and add to the ans
                return summ
            
            return helper(root.left,summ) + helper(root.right,summ) #example 12+13 for left and right

        return helper(root,0)
        
        