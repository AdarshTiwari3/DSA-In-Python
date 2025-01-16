# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None

        def helper(low,high):
            if low>high:
                return None

            mid=(low+high)//2

            root=TreeNode(nums[mid])
            root.left=helper(low,mid-1)
            root.right=helper(mid+1,high)
            return root


        return helper(0,len(nums)-1)