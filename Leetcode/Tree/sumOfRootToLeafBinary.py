# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans=0

        def helper(root,summ):
            # let's do pre order # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans=0

        def helper(root,summ):
            # let's do pre order traversal and get the binary in order from root
            if root is None:
                return
            summ+=str(root.val)
            # calculate if leaf node
            if root.left is None and root.right is None:
                self.ans+=int(summ,2)
                return
            
            helper(root.left,summ)
            helper(root.right,summ)

        helper(root,"")
        return self.ans


            # calculate if leaf node
            if root.left is None and root.right is None:
                self.ans+=int(summ,2)
                return
            
            helper(root.left,summ)
            helper(root.right,summ)

        helper(root,"")
        return self.ans

