#implement a binary tree using python 

class TreeNode:
    def __init__(self,left=None, val=None, right=None):
        self.left=left
        self.val=val
        self.right=right


class BinaryTreeImp:
    def __init__(self):
        self.root=None

    def insertNode(self, val):
        if self.root is None:
            self.root=TreeNode(val=val)
        else:
            self.insertNode(self.root,val)