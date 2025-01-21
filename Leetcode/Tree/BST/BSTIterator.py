# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    #optimised intution - use stack to remove the SC from O(n) to O(h) and always store the left or next smaller element
    def leftMostInorder(self,root):
        while root:
            self.stack.append(root)
            root=root.left
    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        self.leftMostInorder(root)

    def next(self) -> int:
        node=self.stack.pop()

        #check if right is present if yes then go and store all left of it
        if node.right:
            self.leftMostInorder(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack)>0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()