# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        listA=headA
        listB=headB

        while listA is not listB:
            if listA is None:
                listA=headB
            elif listB is None:
                listB=headA
            else :
                listA=listA.next
                listB=listB.next
        return listB