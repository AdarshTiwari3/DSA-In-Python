from typing import List

def findStockSpans(prices: List[int]) -> List[int]:
    # Write your code here.
    stack=[]
    ans=[]
    final_ans=[]
    for i in range(len(prices)):
        # print("i=",prices[i])
        while len(stack)>0 and stack[-1][0]<prices[i]:
            stack.pop()
        # we will store the index of the each next greater element for corresponding elements and if stack is empty will store -1 as an index
        if len(stack)==0:
            ans.append(-1)
        else:
            ans.append(stack[-1][1]) # stores the index in the ans array from the stack

        stack.append((prices[i],i))
    # print(ans)

    for i in range(len(prices)):
        final_ans.append(i-ans[i])
    return final_ans