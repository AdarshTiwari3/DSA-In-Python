# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        slow,fast=head,head
        while ( k > 1):
            fast=fast.next
            k=k-1
        swap1=fast

        while fast.next:
            slow = slow.next
            fast = fast.next
        swap2=slow
        swap1.val, swap2.val=swap2.val, swap1.val

        return head