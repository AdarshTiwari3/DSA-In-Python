from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        ans=0
        for i in range(n-1,1,-1):
            j, k = i-1, 0
            while k < j :
                if nums[j]+nums[k]>nums[i]:
                    ans += (j-k) # because array is sorted the by default it will create triplets
                    j-=1
                else:
                    k+=1


        return ans
    
sol=Solution()
print(sol.triangleNumber([2,2,3,4])) #3