# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2LL(self, l1, l2):
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mergedNode=None
        l1=None
        l2=None
        for i in range(len(lists)):
            l1=lists[i]
            l2=self.merge2LL(l1,l2)
        mergedNode=l2
        return mergedNode
        
        
# time complexity: O(nlogk) where n is the total number of nodes and k is the number of linked lists