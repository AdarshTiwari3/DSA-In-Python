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

        
#optimised solution
import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = tail = ListNode(0)
        for i, node in enumerate(lists):
            if node:
                print("node-",node,"i-",i)
                heapq.heappush(heap, (node.val,i, node)) # values are getting stored in heap, we are using just heapq library

        while heap:
            val,i,node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next: # this is for next node to be inserted
                heapq.heappush(heap, (node.next.val,i, node.next)) #pushing val, node of next node of poped node

        return head.next

#time complexity is O(nlogk) where n is the total number of elements in all linked lists and k is the number of linked lists.
#space complexity is O(k) where k is the number of linked lists using in heap