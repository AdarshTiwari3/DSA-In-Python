from typing import List
import math

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(postOrder: List[int]) -> BinaryTreeNode:
    i = len(postOrder) - 1

    def helper(lowerBound):
        nonlocal i
        if i < 0 or postOrder[i] < lowerBound:
            return None
        rootValue = postOrder[i]
        root = BinaryTreeNode(rootValue)
        i -= 1
        root.right = helper(rootValue)
        root.left = helper(lowerBound)
        return root

    return helper(-math.inf)
