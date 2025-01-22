# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxx=-math.inf
        def helper(root):
            nonlocal maxx
            if root is None:
                return 0

            leftMaxSum=max(helper(root.left),0) # getting max from left helper and 0 to avoid negative numbers as we can't consider it
            rightMaxSum=max(helper(root.right),0)
            maxx=max(maxx,root.val+leftMaxSum+rightMaxSum) # get the max path sum with root+leftSubTree+rightSubTree

            return root.val+max(leftMaxSum,rightMaxSum) # because max(left,right) will give the max sum 


        helper(root)
        return maxx