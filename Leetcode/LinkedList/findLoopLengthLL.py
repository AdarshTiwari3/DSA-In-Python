class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.
def findLength(slow, fast):
    cnt=1
    fast=fast.next
    while slow is not fast:
        cnt=cnt+1
        fast = fast.next
    return cnt

def lengthOfLoop(head: Node) -> int:
    # Write your code here
    slow=head
    fast= head
    
    while fast and fast.next:
        slow = slow.next
        fast=fast.next.next
        if slow == fast:
            return findLength(slow, fast)
    return 0

