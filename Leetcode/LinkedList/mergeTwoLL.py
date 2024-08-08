# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
        temp=ListNode(0)
        ans=temp
        while ( temp1 and temp2):
            if temp1 and temp2 and temp1.val <= temp2.val:
                ans.next=temp1
                temp1=temp1.next
            elif temp1 and temp2 and temp2.val<temp1.val:
                ans.next=temp2
                temp2=temp2.next
            ans=ans.next
        

        if temp1 and not temp2:
            ans.next=temp1
            ans= ans.next
        elif not temp1 and temp2:
            ans.next=temp2
            ans=ans.next
        # print("ans=", ans.val)
        return temp.next