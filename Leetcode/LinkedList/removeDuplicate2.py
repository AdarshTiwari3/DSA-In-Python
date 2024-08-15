# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=ListNode(0)
        ans=prev
        curr=head
        
        while curr :
            if curr.next and curr.val == curr.next.val: 
                while curr.next and curr.val==curr.next.val:
                    curr=curr.next
                prev.next=curr.next
            else:
                prev.next=curr
                prev=prev.next
            curr=curr.next

        return ans.next