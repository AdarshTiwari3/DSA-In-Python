from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # next greater element to right
        stack=[]
        ans=[]
        i=len(temperatures)-1
        while i>=0:
            cnt=1
            while stack and stack[-1][0]<=temperatures[i]:
                cnt+=stack[-1][1]
                stack.pop()
            # print("cnt=",cnt)
            if stack==[]:
                ans.append(0)
            else:
                ans.append(cnt)
            stack.append((temperatures[i],cnt))

            i-=1
        return ans[::-1]
    

sol=Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73])) #[1,1,4,2,1,1,0,0]
        