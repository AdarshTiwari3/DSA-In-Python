# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=ListNode(0)
        oddCurr=odd
        even=ListNode(0)
        evenCurr=even
        curr=head
        count=1
        while curr:
            # print("count-",count)
            if count%2 ==1:
                print('curr-odd=',curr.val)
                oddCurr.next=curr
                oddCurr=oddCurr.next
                
            elif count%2==0:
                print("curr-",curr.val)
                evenCurr.next=curr
                # print("Even-",even)
                evenCurr=evenCurr.next
            
            count+=1
            curr=curr.next
        # print("EvenCurr=",evenCurr)
        # put the None in the last of evenCurr otherwise it will still point the value of head
        evenCurr.next=None
        # now add the oddCurr to even.next
        # print("Even=",even)
        oddCurr.next=even.next

        return odd.next
        