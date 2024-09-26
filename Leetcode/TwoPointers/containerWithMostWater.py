from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #intuition-
        #1. maintain left and right pointer and calculate the area for min b/w left and right and its indexes
        n=len(height)
        left, right, mArea = 0, n-1, 0

        while left < right:
            mArea = max( mArea, min( height[left], height[right]) * ( right - left ))

            if height[left] <= height[right]:
                left+=1
            else:
                right-=1
        
        return mArea
    
sol=Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7])) #49
