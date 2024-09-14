from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=len(nums)-1
        i=0
        while i <= j:
            if nums[i]==val:
                nums[i], nums[j]= nums[j], nums[i]
                j-=1
            else:
                i+=1

        return j+1
    
sol=Solution()
print(sol.removeElement([3,2,2,3],3)) #2