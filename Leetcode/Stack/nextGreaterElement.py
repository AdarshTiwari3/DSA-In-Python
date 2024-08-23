from typing import List

def nextGreaterElement(arr: List[int], n: int) -> List[int]:
    # Write your code here.
    stack=[]
    ans=[]
    i=len(arr)-1
    while i>=0:
        while len(stack)>0 and stack[-1]<=arr[i]: #pop the smaller element from stack so that we can get larger
            stack.pop()
        if len(stack)==0 or stack == []: # if stack is empty after pop then put -1
            ans.append(-1)
        else:
            #put the greater element if we have found any
            ans.append(stack[-1])

        stack.append(arr[i])


        i-=1

    return ans[::-1]


check=nextGreaterElement([1,3,2,4],4)
print(check) #[3,4,4,-1]