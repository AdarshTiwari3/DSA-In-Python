# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self,head):
        curr=head
        prev=None
        while curr:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        return prev
    def findMiddleNode(self,head):
        slow=fast=head
        fast=fast.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr=head
        middleNode=self.findMiddleNode(curr)
        nextNode=middleNode.next
        middleNode.next=None
        reversedNode=self.reverseLL(nextNode)
        curr=head
        ans=ListNode(0)
        final_ans=ans
        while curr and reversedNode:
            if curr:
                ans.next=curr
                ans=ans.next
                curr=curr.next
            if reversedNode:
                ans.next=reversedNode
                ans=ans.next
                reversedNode=reversedNode.next
        if curr:
            ans.next=curr
        if reversedNode:
            ans.next=reversedNode
        head=final_ans.next
            
        