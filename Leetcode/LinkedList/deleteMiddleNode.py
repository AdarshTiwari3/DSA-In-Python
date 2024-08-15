# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow = head
        fast = head
        fast = fast.next.next
        # first move fast so that slow will point to before the middle or actual
        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
        
        # now slow will be at before middle , just change the links
        slow.next=slow.next.next
        return head
    

