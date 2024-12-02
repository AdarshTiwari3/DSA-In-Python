#implement a binary tree using python 

class TreeNode:
    def __init__(self,left=None, val=None, right=None):
        self.left=left
        self.val=val
        self.right=right


class BinaryTreeImp:
    def __init__(self):
        self.root=None

    def insertANode(self, val):
        if self.root is None:
            self.root=TreeNode(val=val)
        else:
            self.insertNode(self.root,val)

    def insertNode(self, curr, val):
        queue=[curr]
        #level order technique
        while queue:
            node=queue.pop(0)
            if node.left is None:
                node.left=TreeNode(val=val)
                return
            else:
                queue.append(node.left)

            if node.right is None:
                node.right=TreeNode(val=val)
                return
            else:
                queue.append(node.right)

    def traversal_inorder(self,node):
        if node:
            self.traversal_inorder(node.left)
            print(node.val,end='->')
            self.traversal_inorder(node.right)


tree=BinaryTreeImp()
tree.insertANode(10)
tree.insertANode(5)
tree.insertANode(15)
tree.traversal_inorder(tree.root)
