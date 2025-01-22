# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def makeParent(self,root,parents):
        q=deque([root])

        while q:
            node=q.popleft()
            if node.left:
                parents[node.left]=node
                q.append(node.left)
            if node.right:
                parents[node.right]=node
                q.append(node.right)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents={}
        self.makeParent(root,parents)
        
        q=deque([target])
        visited=set([target])
        curr_level=0
        ans=[]
        while q:
            if curr_level==k:
                #push the values of queue to ans array as we have reached at desired level
                for node in q:
                    ans.append(node.val)
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if node.left and not node.left in visited: #move left node
                    visited.add(node.left)
                    q.append(node.left)
                if node.right and not node.right in visited: #move right
                    visited.add(node.right)
                    q.append(node.right)
                if node in parents and not parents[node] in visited:
                    visited.add(parents[node])
                    q.append(parents[node])

            curr_level+=1

        return ans