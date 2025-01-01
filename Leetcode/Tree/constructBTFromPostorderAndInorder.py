# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,inorder,postorder,inorderMap,startIn,endIn,startPost,endPost):
        if startIn > endIn or endPost<startPost:
            return None

        root=TreeNode(val=postorder[endPost])

        rootIndex=inorderMap[root.val]

        leftSize=rootIndex-startIn
        
        root.left=self.helper(inorder,postorder,inorderMap,startIn,rootIndex-1,startPost,startPost+leftSize-1)

        root.right=self.helper(inorder,postorder,inorderMap,rootIndex+1,endIn,startPost+leftSize,endPost-1)




        return root
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:        
        inorderMap={}
        for i in range(len(inorder)):
            inorderMap[inorder[i]]=i

        # print("map=",inorderMap)
        return self.helper(inorder,postorder,inorderMap,0,len(inorder)-1,0,len(postorder)-1)

        