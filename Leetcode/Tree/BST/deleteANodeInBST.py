# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLastRightNode(self,root):
        if root.right is None:
            return root
        return self.findLastRightNode(root.right)
    def helper(self,root):
        #check the 3 condition for deletion 1. one child, 2. two child, 3. No child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        else:
            # if both child is present break with one and connect with last of right node of right of left to left child

            rightNode=root.right
            lastRightNode=self.findLastRightNode(root.left)
            # join the links
            lastRightNode.right=rightNode
            return root.left # because of new link's been created


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # three type of deletion can be done
        #1. if node is leaf then just break the connect with parent
        #2. if one child is available then just point to that child
        #3. if both child is available - this is bit tricky . here we can swap the nodes and links
        if root is None:
            return None

        # check if root is key
        if root.val==key:
            return self.helper(root)

        curr=root
        while curr:
            if curr.val>key:
                #need to move left
                #check if curr.left is key or not else move curr
                if curr.left and curr.left.val==key:
                    curr.left=self.helper(curr.left) # delete the curr.left and point to next of it    
                curr=curr.left
            elif curr.val<key:
                # need to move right
                # check same as if for curr.right
                if curr.right and curr.right.val==key:
                    curr.right=self.helper(curr.right)
                curr=curr.right
        return root

        