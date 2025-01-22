# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,arr):
        if root!=None:
            self.inorder(root.left,arr)
            arr.append(root.val)
            self.inorder(root.right,arr)
    def buildTree(self,arr,low,high):
        if low > high:
            return None
        mid = (low+high)//2
        root = TreeNode(arr[mid])
        root.left = self.buildTree(arr,low,mid-1)
        root.right = self.buildTree(arr,mid+1,high)
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.inorder(root,arr)
        root = self.buildTree(arr,0,len(arr)-1)
        return root