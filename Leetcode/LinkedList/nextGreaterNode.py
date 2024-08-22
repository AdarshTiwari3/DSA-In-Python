# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next

        ans=[]
        stack=[]
        i=len(arr)-1
        while i>=0:
            if stack==[]:
                ans.append(0)
            elif len(stack) and stack[-1]>arr[i]:
                ans.append(stack[-1])
            elif len(stack) and stack[-1]<=arr[i]:
                while len(stack) and stack[-1] <= arr[i]:
                    stack.pop()
                if len(stack)==0:
                    ans.append(0)
                else:
                    ans.append(stack[-1])
            stack.append(arr[i])
            i-=1
        return reversed(ans)
