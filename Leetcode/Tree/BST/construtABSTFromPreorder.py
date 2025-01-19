# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not len(preorder):
            return None

        i=0 # for preorder array traversal

        def helper(upperBound):
            nonlocal i
            if i==len(preorder) or preorder[i]>upperBound:
                # exit as out of bound 
                return None
            root=TreeNode(preorder[i]) 
            i+=1 # move to next index
            root.left=helper(root.val)  # left subtree should less than round means upperbound will be root.val
            root.right=helper(upperBound) # right will be upper bound as it should be more than root.val so remain unchanged

            return root



        return helper(math.inf) 