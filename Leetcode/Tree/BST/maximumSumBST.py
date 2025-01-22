# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maxSum=0
        def helper(root):
            nonlocal maxSum
            if root is None:
                return (True, -math.inf,math.inf,0) # # (isBST, max, min, sum)
           

            isLeftBST,leftMax,leftMin,leftSum=helper(root.left)
            isRightBST,rightMax,rightMin,rightSum=helper(root.right)

            if not isLeftBST or not isRightBST or leftMax >= root.val or rightMin <= root.val:
                return (False, 0, 0, 0)  # Invalid BST


            summ=leftSum+root.val+rightSum
            maxSum=max(maxSum,summ)

            return (True,max(root.val,rightMax),min(root.val,leftMin),summ)
        helper(root)
        return maxSum