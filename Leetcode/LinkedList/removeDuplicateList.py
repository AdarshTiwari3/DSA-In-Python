# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        temp=curr
        ans=curr
        while curr:
            while curr  and temp and curr.val == temp.val:
                temp=temp.next #skip the element
            print("temp=",curr.val)
            curr.next=temp
            curr=curr.next
        
        return ans
        