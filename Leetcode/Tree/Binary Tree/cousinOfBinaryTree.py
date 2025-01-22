# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None:
            return True
        queue=[root]
        Xp,Yp = None,None

        while queue:
            for i in range(len(queue)):
                node=queue.pop(0)

                if node.left:
                    queue.append(node.left)
                    if node.left.val==x:
                        Xp=node
                    if node.left.val==y:
                        Yp=node
                
                if node.right:
                    queue.append(node.right)
                    if node.right.val==x:
                        Xp=node
                    if node.right.val==y:
                        Yp=node
                # keep check on the same depth
                # check for same parent
                if Xp and Yp:
                    return Xp!=Yp
            # print("Xp=",Xp,"Yp=",Yp)
            if (Xp is None and Yp) or (Yp is None and Xp):
                return False

        return False