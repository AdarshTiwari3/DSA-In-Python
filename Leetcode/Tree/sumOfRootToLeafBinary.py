# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
<<<<<<< HEAD

=======
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
>>>>>>> b0f562bcac6c412fd15671b6c7e13ec3284b5f55
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


<<<<<<< HEAD
            
=======
            # calculate if leaf node
            if root.left is None and root.right is None:
                self.ans+=int(summ,2)
                return
            
            helper(root.left,summ)
            helper(root.right,summ)

        helper(root,"")
        return self.ans

>>>>>>> b0f562bcac6c412fd15671b6c7e13ec3284b5f55
