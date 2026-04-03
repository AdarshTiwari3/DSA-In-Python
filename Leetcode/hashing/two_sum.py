from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ans = []

        n = len(nums)
        mp = {}

        for i in range(n):

            if target - nums[i] in mp:
                ans.append(mp[target - nums[i]])
                ans.append(i)

            mp[nums[i]] = i

        return ans


"""
TC=> O(n)
SC=> O(n) # Hashmap 
"""
