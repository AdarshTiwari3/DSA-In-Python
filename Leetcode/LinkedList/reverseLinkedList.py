# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self,head):
        prev=None
        curr=head
        # nextNode=head

        while curr:
           nextNode=curr.next
           curr.next=prev
           prev=curr
           curr=nextNode
    


            # curr=curr.next
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        
        return self.reverseLinkedList(head)
        