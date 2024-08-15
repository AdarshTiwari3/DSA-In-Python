# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self,head, n):
        curr=head
        prev=None
        while curr and n:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
            n-=1
        return curr, prev
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        l=left
        r=right
        prev=None
        while left>1:
            left-=1
            prev=curr
            curr=curr.next
        # now curr is on left position
        nextNode,reversedNode=self.reverseLL(curr,r-l+1)
        print("nextNode-",nextNode,"reversedLL-",reversedNode,"curr",curr)
        if prev:
            prev.next=reversedNode
        else : 
            head=reversedNode
        curr.next=nextNode
        return head
