# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if root is None:
            return ans
        queue=[]
        queue.append(root)
        while queue:
            size=len(queue)
            print("size=",size)
            levelArray=[]
            for i in range(size):
                node=queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                levelArray.append(node.val)
            ans.append(levelArray)
            # print("Local=",levelArray)
            # print("queue=",queue)
        return ans
        