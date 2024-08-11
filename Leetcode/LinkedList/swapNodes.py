# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        slow,fast=head,head
        while ( k > 1):
            fast=fast.next
            k=k-1
        swap1=fast

        while fast.next:
            slow = slow.next
            fast = fast.next
        swap2=slow
        swap1.val, swap2.val=swap2.val, swap1.val

        return head
    

#using recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapRecursion(self,head):
        if head is None or head.next is None:
            return head
        firstNode=head
        secondNode=head.next
        nextPairNode=secondNode.next
        firstNode.next=self.swapRecursion(nextPairNode) # put the link of the next pair in the first.next
        secondNode.next=firstNode
        # now after swapping the second node will be the head
        return secondNode

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swapRecursion(head)