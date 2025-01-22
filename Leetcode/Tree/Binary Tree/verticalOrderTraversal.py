# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if root is None:
            return ans
        columnMap=defaultdict(list) # it will create a dictionary key if it is not present, a new empty list will be created--- example { "key1":[1,2,3]}, we are gonna store key as column index, (level and node)
        q=deque([(root,0,0)]) #root, level, column

        while q:
            node,level,col=q.popleft()
            columnMap[col].append((level,node.val))
            if node.left:
                q.append((node.left,level+1, col-1))

            if node.right:
                q.append((node.right,level+1,col+1))


        for col in sorted(columnMap.keys()):
            columnMap[col].sort()

            ans.append([nodeVal for level,nodeVal in columnMap[col]])

        return ans