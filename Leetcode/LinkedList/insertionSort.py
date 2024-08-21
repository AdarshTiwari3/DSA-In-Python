# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode(0,head) #created a node and its pointing the head
        prev=ans
        final_ans=ans
        curr=head

        while curr:
            if curr.next and curr.val > curr.next.val:
                # insertion happens here
                while prev.next and prev.next.val < curr.next.val:
                    prev=prev.next
                
                tmp=prev.next
                prev.next=curr.next
                curr.next=curr.next.next
                prev.next.next=tmp
                prev=ans

            else:
                curr=curr.next
        return final_ans.next