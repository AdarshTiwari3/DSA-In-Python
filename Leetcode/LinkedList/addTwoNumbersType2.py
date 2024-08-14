# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, head):
        if head is None or head.next is None:
            return head
        curr = head
        prev=None
        while curr:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            
            list1=self.reverseLL(l1)
            list2=self.reverseLL(l2)
            print("List-1",list1)
            ans = ListNode(-1)
            final_ans=ans
            carry=0
            while list1 or list2:
                sum = carry
                if list1:
                    sum += list1.val
                    list1=list1.next
                if list2:
                    sum += list2.val
                    list2=list2.next
                carry=sum//10
                newNode=ListNode(sum%10)
                print("sum=",sum, "Node-",newNode)
                ans.next = newNode
                ans=ans.next
            # if carry has some value means we need to create one more node and point to the ans
            if carry:
                ans.next=ListNode(carry)
                ans=ans.next
            return self.reverseLL(final_ans.next)