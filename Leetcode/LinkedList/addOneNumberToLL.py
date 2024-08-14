#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def helper(self,head):
        if head is None:
           return 1 # base case as carry =1
        
        carry=self.helper(head.next) # return the value of the carry
        # now check the data 
        head.data+=carry
        if head.data < 10 : # no carry , break the recursion
            return 0 # return carry = 0 
        
        head.data = 0 # 0 with the value and 1 goes in carry , why zero because maximum it can go to 1+9 = 10
        return 1 # carry = 1
        
    
    def addOne(self,head):
        #Returns new head of linked List.
        carry = self.helper(head)
        
        # check if we have carry remain 1 even after doing all stuffs - means need to create a node
        
        if carry:
            newNode=Node(carry)
            newNode.next=head
            head=newNode
        return head
            
        
        


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