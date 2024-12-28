# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev=None
        def helper(root):
            if root is None:
                return 

            helper(root.right)
            helper(root.left)
            root.right=self.prev
            root.left=None
            self.prev=root
        helper(root)
        return root
        
        

        
# solution 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr=root
        #using morris traversal technique
        while curr:
            # go to the right most of the left child and add to the right child ofthe root
            if curr.left:
                temp=curr.left
                while temp.right:
                    temp=temp.right
                
                temp.right=curr.right # add the links to the right child of the root

                curr.right=curr.left # add to the right for root.left child

                curr.left=None #now break the link of left child
            curr=curr.right

