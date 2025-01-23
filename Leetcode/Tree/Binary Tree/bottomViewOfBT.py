from typing import List
from collections import deque
# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottomView(root: BinaryTreeNode) -> List[int]:
    # Write your code here.
    if root is None:
        return []
    
    q=deque([(root,0)])
    mp={}
    while q:
        node,col=q.popleft()
        #always update the map with latest value
        if node:
            mp[col]=node.data

        if node.left:
            q.append((node.left,col-1))
        if node.right:
            q.append((node.right,col+1))
    bottom_view=[mp[col] for col in sorted(mp.keys())]
    return bottom_view