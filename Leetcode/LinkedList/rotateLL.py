# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        curr=head
        tNode=1
        while curr and curr.next:
            curr=curr.next
            if curr:
                tNode+=1
        if k==tNode:
            return head        
        curr.next=head
        curr=curr.next
        if k>tNode:
            k=k%tNode
        # curr=head
        
        check=tNode-k
        print("check=",tNode-k,"tNode=",tNode)
        while curr and check>1:
            check-=1
            curr=curr.next
        print("curr=",curr)
        head=curr.next
        curr.next=None

        return head