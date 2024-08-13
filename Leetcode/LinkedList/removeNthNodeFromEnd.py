# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if head is None :
        #     return head
        # if head.next is None and n==1:
        #     return None
        
        fast=head
        cnt=n
        while fast and cnt>0:
            cnt=cnt-1
            fast=fast.next
        slow=head
        if fast is None :
            # means we have to delete head
            head=head.next
            return head
        while fast.next: 
            slow=slow.next
            fast=fast.next
        #now slow will point to the prev of Nth node
        print("slow=",slow.val)
        
        slow.next=slow.next.next

        return head
        

