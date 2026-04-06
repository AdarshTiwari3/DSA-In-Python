from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = 0
        mp = {0: 1}
        ans = 0

        for num in nums:
            prefix += num

            key = prefix - goal

            if key in mp:
                ans += mp[key]

            mp[prefix] = mp.get(prefix, 0) + 1

        return ans


# TC=> O(n)
# SC=> O(n)
