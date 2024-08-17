# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr=head
        ans1=ListNode(0)
        ans2=ListNode(0)
        part1=ans1
        part2=ans2
        while curr:
            if curr.val < x:
                part1.next=curr
                part1=part1.next
            else:
                part2.next=curr
                part2=part2.next
            curr=curr.next
        print("part1=",part1,"part2=",part2)
        part2.next=None
        part1.next=ans2.next
        return ans1.next

