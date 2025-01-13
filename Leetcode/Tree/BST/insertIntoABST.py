# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node=TreeNode(val)
        if root is None:
            return node
        curr=root
        while True:

            if val > curr.val:
                # move right
                # check if right is None then insert a new node 
                if curr.right is None:
                    curr.right=node
                    break
                curr=curr.right
            else:
                # move left and check if left is none or not, if none insert the node
                if curr.left is None:
                    curr.left=node
                    break
                curr=curr.left

        return root