# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def makeParents(self,root,parents,start):
        if root is None:
            return 
        q=deque([root])
        targetNode=None
        while q:
            node=q.popleft()
            if node and node.val==start:
                targetNode=node
            if node.left:
                parents[node.left]=node
                q.append(node.left)
            if node.right:
                parents[node.right]=node
                q.append(node.right)
        return targetNode

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        #first make parents
        parents={}
        targetNode=self.makeParents(root,parents,start)
        # print("target=",targetNode)
        if targetNode is None:
            return 0
        seen=set([targetNode])
        # seen.add(targetNode)
        q=deque([targetNode]) #(target)
        time=0
        while q:
            n=len(q)
            for i in range(n):
                node=q.popleft()
                if node.left and node.left not in seen:
                    q.append(node.left)
                    #mark visited
                    seen.add(node.left)
                if node.right and node.right not in seen:
                    q.append(node.right)
                    #mark visited
                    seen.add(node.right)
                if node in parents and parents[node] not in seen:
                    # check upwards in parents map and mark it visited
                    q.append(parents[node]) #in our test case it will be first 1
                    seen.add(parents[node])
                
            time+=1 # as it has completed a step for check left,right and upwards
        return time-1 # as it has counted the time for when cases were none in the last