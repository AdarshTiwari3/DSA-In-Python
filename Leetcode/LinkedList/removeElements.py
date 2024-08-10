# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
            if head is None:
                return head
        
            prev=ListNode(0)
            prev.next=head
            ans=prev
            temp = head
            while temp:
                if temp and temp.val==val:
                   prev.next=temp.next
                else:
                    prev=temp
                temp=temp.next
            return ans.next