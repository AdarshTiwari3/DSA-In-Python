from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # find the next smaller to right
        stack=[]
        ans=[]
        i=len(prices)-1
        while i>=0:
            while stack and stack[-1]>prices[i]:
                stack.pop()
            if stack == []:
                ans.append(0)
            else:
                ans.append(stack[-1])
            stack.append(prices[i])
            i-=1
        
        final_ans=ans[::-1]
        for i in range(len(final_ans)):
            final_ans[i]=prices[i]-final_ans[i]

        return final_ans

sol=Solution()
print(sol.finalPrices([8,4,6,2,3])) #[4,2,4,2,3]