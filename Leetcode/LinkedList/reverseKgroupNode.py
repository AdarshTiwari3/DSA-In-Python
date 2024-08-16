# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self,head):
        curr=head
        prev=None
        while curr:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        return prev
    def findKthNode(self,head, k):
        curr=head
        while curr and k>1:
            curr=curr.next
            k-=1
        return curr
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        # temp=curr
        prevNode=None
        nextNode=None
        n=k
        while curr:
            kthNode=self.findKthNode(curr,n)
            # print("kthNode=",kthNode)
            # print("curr=",curr)
            if kthNode==None:
                break
            else:
                # print("curr=",curr)
                nextNode=kthNode.next
                kthNode.next=None
                reversedNode=self.reverseLL(curr)
                print("reversedNode=",reversedNode)
                if prevNode is None:
                    head=reversedNode
                else:
                    prevNode.next=reversedNode
                curr.next=nextNode
                prevNode=curr
                curr=nextNode
        return head