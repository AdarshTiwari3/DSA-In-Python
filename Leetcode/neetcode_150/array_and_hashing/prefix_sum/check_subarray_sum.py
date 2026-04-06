from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0: -1}
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num

            key = (prefix) % k
            if key in mp:
                if i - mp[key] >= 2:
                    return True

            else:
                mp[key] = i

        return False


# TC=> O(n)
# SC=> O(n)
