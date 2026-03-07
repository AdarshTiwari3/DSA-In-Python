from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            # base case if node is none return 0, 0
            if node is None:
                return (0, 0)  # rob and skip

            left_rob, leftskip = helper(node.left)
            right_rob, rightskip = helper(node.right)

            # rob current node
            rob = node.val + leftskip + rightskip

            # if skip the current node

            skip = max(left_rob, leftskip) + max(
                right_rob, rightskip
            )  # because want the max robbery
            return (rob, skip)

        return max(helper(root))


# TC=> O(n) SC=O(n)
