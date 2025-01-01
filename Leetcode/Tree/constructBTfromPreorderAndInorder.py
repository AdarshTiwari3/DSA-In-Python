# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,preorder,inorder,inorderMap,startPre,endPre,startIn,endIn):
        if startPre>endPre or startIn>endIn:
            return None
        root=TreeNode(val=preorder[startPre])

        rootIndex=inorderMap[preorder[startPre]]

        leftSize=rootIndex-startIn

        root.left=self.helper(preorder,inorder,inorderMap,startPre+1,startPre+leftSize,startIn,rootIndex-1)
        root.right=self.helper(preorder,inorder,inorderMap,startPre+leftSize+1,endPre,rootIndex+1,endIn)
        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap={}
        for i in range(len(inorder)):
            inorderMap[inorder[i]]=i
        
        return self.helper(preorder,inorder,inorderMap,0,len(preorder)-1,0,len(inorder)-1)
        
    