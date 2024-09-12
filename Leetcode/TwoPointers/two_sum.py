from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        ans=[]
        for i in range(len(nums)):
            if target-nums[i] in mp.keys():
                ans.append(i)
                ans.append(mp[target-nums[i]])
                return ans
            mp[nums[i]]=i
        
        return ans
    

sol=Solution()
print(sol.twoSum([2,7,11,15],9)) #[0,1] or [1,0]