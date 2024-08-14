# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow= head
        fast=head
        
        while fast and fast.next:
            # print("hi")
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast: return None # returns None if no cycle found
            # print("slow-",slow.val)
        # print("slow-",slow.val)
        slow=head
        while slow != fast:
            slow=slow.next
            fast=fast.next
        if slow == fast:
            return slow
        # return None
        