# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseLL(self, head):
        if not head or not head.next:
            return head
        else:
            prev=None
            curr=head
            while curr:
                nextNode=curr.next
                curr.next=prev
                prev=curr
                curr=nextNode
            return prev
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        head2=self.reverseLL(slow)
        print("Slow-",slow.val)
        
        fast=head
        while head2 and fast:
            if head2.val != fast.val:
                return False
            head2=head2.next
            fast=fast.next
        return True
        