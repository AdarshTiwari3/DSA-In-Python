from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, left, right = 0, 0, len(nums)-1

        while i <= right:
            if nums[i]==0:
                nums[left],nums[i]=nums[i], nums[left]
                left += 1
            elif nums[i]==2:
                nums[right], nums[i]= nums[i], nums[right]
                right-=1
                i-=1
            # print(nums)
            i+=1
        
        return nums
    
sol=Solution()
print(sol.sortColors([2,0,2,1,1,0])) #[0,0,1,1,2,2]