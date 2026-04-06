from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0: -1}

        prefix = 0
        ans = 0

        # logic is here to convert 0 in -1 and 1 as +1 so that the equal number of 0's and 1's will always have sum = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in mp:
                ans = max(ans, i - mp[prefix])

            else:
                mp[prefix] = i

        return ans


# TC=> O(n)
# SC=> O(n)
