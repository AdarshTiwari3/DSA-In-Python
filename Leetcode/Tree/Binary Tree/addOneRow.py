# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val,left=root)

        def helper(node,curr_depth):
            if node is None:
                return
            # if we reach at the required depth
            if depth-1 == curr_depth:
                node.left=TreeNode(val=val,left=node.left)
                node.right=TreeNode(val=val,right=node.right)
                return


            helper(node.left,curr_depth+1)
            helper(node.right,curr_depth+1)

        helper(root,1)
        return root