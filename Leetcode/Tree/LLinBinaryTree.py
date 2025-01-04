# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if head is None:
            return True
        def helper(root,head):
            if root is None:
                return False
            if head is None:
                return True
            if root.val==head.val:
                
                if head.next is None:
                    return True
                else:
                    return helper(root.left,head.next) or helper(root.right,head.next)
            
            return False


        return helper(root,head) or self.isSubPath(head,root.left) or self.isSubPath(head,root.right)