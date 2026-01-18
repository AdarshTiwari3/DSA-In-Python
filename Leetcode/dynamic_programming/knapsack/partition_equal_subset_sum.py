from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ=sum(nums)
        if summ%2==1:
            return False

        target=summ//2

        dp=[False] * (target+1)

        dp[0]=True #base case

        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1): #goes from target to nums[i] and get the valid target
                dp[j]=dp[j] or dp[j-nums[i]]
        
        return dp[target]
    
sol=Solution()
ans=sol.canPartition([1,6,5,12])
print("ans=",ans)
        