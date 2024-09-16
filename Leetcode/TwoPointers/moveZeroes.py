from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        while i<=len(nums)-1:
            if nums[i]:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
                j+=1
            else:
                i+=1
        
        return nums

sol=Solution()
print(sol.moveZeroes([0,1,0,3,12])) #[1,3,12,0,0]
    