from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        summ=nums[0]+nums[1]+nums[2]
        
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1

            while j < k:
                curr_sum=nums[i]+nums[j]+nums[k]
                if abs(target-curr_sum)<abs(target-summ):
                    summ=curr_sum
                
                if curr_sum < target:
                    j+=1
                else:
                    k-=1
        
        return summ
    
sol=Solution()
print(sol.threeSumClosest([-1, 2, 1, -4],1)) #2