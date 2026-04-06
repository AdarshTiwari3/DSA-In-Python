from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0

        mp = {
            0: 1
        }  # if sum - k == 0 means subarray is same as k e.g k=3 and subarray is [3]
        ans = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in mp:
                ans += mp[
                    prefix_sum - k
                ]  # if multiple times subarray exists like [1, -1], [0] and [1, -1, 0] all has same key 0

            if prefix_sum in mp:
                mp[prefix_sum] += 1
            else:
                mp[prefix_sum] = 1
        return ans


# TC=> O(n)
# SC=> O(n)
