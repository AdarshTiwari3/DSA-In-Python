from typing import List
import math

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        total_sum=sum(nums)

        n=len(nums)

        sum1=total_sum//2

        dp=[False]*(sum1+1) #take the first half

        dp[0]=True # base case

        #. calculate the possible sum from 1 to total_sum range --> 1D dp of subset sum
        
        for i in range(n):
            
            for j in range(sum1, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i]]


        minn=math.inf
        
        for i in range(sum1,-1,-1):
            if dp[i]:
                minn=min(minn, total_sum-(2*i))
                break

        return minn

sol=Solution()
ans=sol.minimumDifference([1,6,5,11])
print("ans=",ans) # 12-11 = 1
ans2=sol.minimumDifference([1,2,7])
print("ans=",ans2) # 7-3 = 4 or range-2*left_sum(best possible from first half) = 10-(2*3)=10-6=4 ans