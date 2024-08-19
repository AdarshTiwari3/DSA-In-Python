# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2LL(self,l1,l2):
        ans=ListNode(0)
        final_ans=ans
        while l1 and l2:
            if l1.val < l2.val:
                ans.next=l1
                ans=ans.next
                l1=l1.next
            else:
                ans.next=l2
                ans=ans.next
                l2=l2.next
        if l1:
            ans.next=l1
        if l2:
            ans.next=l2
        return final_ans.next
    def findMiddle(self,head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def mergeSort(self,head):
        #using merge sort
        if head is None or head.next is None:
            return head
        middle=self.findMiddle(head)
        # print("mid=",middle)
        left=head
        right=middle.next
        middle.next=None
        # now will call left and right recursion
        # for left it goes to left-mid and for right it goes to mid+1- right
        left=self.mergeSort(left) # it always give the sorted left portion
        right=self.mergeSort(right) # this gives right sorted portion
        return self.merge2LL(left,right)
       
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head=self.mergeSort(head)
        return head