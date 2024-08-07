# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        ans=0
        if temp.next is None:
            return temp.val
        else :
            while temp is not None:
                ans = ans<<1 | temp.val # or operator works like addition if both are odd
                print('ans=',ans)
                # print(4 | 9)
                temp = temp.next
                
        return ans