#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverseLL(self,head):
        curr=head
        prev=head
        while curr:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        return prev
    def addOne(self,head):
        #Returns new head of linked List.
        reversedNode=self.reverseLL(head)
        temp=reversedNode
        while temp:
            carry=1
            temp.data = temp.data + carry
            
            if temp.data < 10:
                carry=0
                break
            else :
                carry = 1
                temp.data=0
            temp=temp.next
        reversedNodeAfter=None
        if carry==1:
            newNode=Node(carry)
            reversedNodeAfter=self.reverseLL(reversedNode)
            newNode.next=reversedNodeAfter
        reversedNodeAfter=self.reverseLL(reversedNode)
        return reversedNodeAfter
                
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next


def PrintList(head):
    while head:
        print(head.data, end='')
        head = head.next


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        list1 = LinkedList()
        arr = list(map(int, input().strip().split()))
        for i in arr:
            list1.insert(i)

        resHead = Solution().addOne(list1.head)
        PrintList(resHead)
        print()

# } Driver Code Ends