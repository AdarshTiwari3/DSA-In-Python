class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        small = greater = prev = None
        def inorder(root):
            nonlocal small, greater, prev
            if root is None:
                return
            inorder(root.left)
            if prev and prev.val > root.val:
                # found first voilation of BST
                small = root
                if not greater:
                    greater = prev
            prev = root
            inorder(root.right)

        inorder(root)
        small.val, greater.val = greater.val, small.val