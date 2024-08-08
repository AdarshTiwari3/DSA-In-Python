# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self,head):
        prev=None
        curr=head
        # nextNode=head

        while curr:
           nextNode=curr.next
           curr.next=prev
           prev=curr
           curr=nextNode
    


            # curr=curr.next
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        
        return self.reverseLinkedList(head)
    

    #using recursion
    def reverseLL(self, head):
        if head is None or head.next == None:
            return head
        else:
            # print("node-",head.val)
            reversedNode=self.reverseLL(head.next)
            front=head.next
            front.next=head # lets take a case as node [4,5] now head.next.next=head - this will reverse the links and for head.next put none there
            head.next=None
        
        

            # print("head-",reversedNode.val,"check=",front.val)
            return reversedNode    
        
        