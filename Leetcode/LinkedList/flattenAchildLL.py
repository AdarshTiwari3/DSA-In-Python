class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.
def merge2LL(l1,l2):
    ans=Node(0)
    final_ans=ans
    while l1 and l2:
        if l1.data < l2.data:
            ans.child=l1
            ans=l1
            l1=l1.child
        else:
            ans.child=l2
            ans=l2
            l2=l2.child
        ans.next=None
    # list has something remaining
    if l1:
        ans.child=l1
    else:
        ans.child=l2
    return final_ans.child

def flattenLinkedList(head: Node) -> Node:
    # Write your code here
    if head is None or head.next is None:
        return head
    
    mergedNode=flattenLinkedList(head.next)
    # now merge the head with head.next and treat both as a merging of two LL and make new merged list as a head
    head=merge2LL(head,mergedNode)

    return head

