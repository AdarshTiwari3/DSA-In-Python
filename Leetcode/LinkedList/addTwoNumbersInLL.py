# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1,temp2 = l1,l2
        ans = ListNode(0)
        final_ans=ans
        carry=0
        while temp1 or temp2:
            sum=carry
            if temp1:
                sum=sum + temp1.val
                # print("sum=",sum)
            if temp2:
                sum=sum + temp2.val
                # print("sum2=",temp2.val)
            newNode=ListNode(sum%10)
            carry=sum//10
            # links the new node to ans
            print("NewNode=",newNode)
            ans.next=newNode
            ans=ans.next
            if temp1:
                temp1=temp1.next
            if temp2:
                temp2=temp2.next

        if carry:
            newNode=ListNode(carry)
            ans.next=newNode
            ans=ans.next
            
        return final_ans.next