from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp={}
        ans=[]
        for i in range(len(nums1)):
            mp[nums1[i]]=1
        # print("map=",mp)
        for i in range(len(nums2)):
            if nums2[i] in mp and mp[nums2[i]]:
                mp[nums2[i]]=0
                ans.append(nums2[i])
            # print("map2=",mp)
        return ans
    
sol=Solution()
print(sol.intersection([1,2,2,1],[2,2])) #[2]

#optimized solution
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        return list(nums1 & nums2)
    
sol=Solution()
print(sol.intersection([1,2,2,1],[2,2])) #[2]