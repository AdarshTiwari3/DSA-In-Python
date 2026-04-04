from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        prefix = 0
        ans = 0
        mp = {0: 1}

        for num in nums:
            prefix += num

            remainder = (
                prefix % k
            )  # because subarray_sum should be prefix[j]-prefix[i] and sum %k ==0 hence (prefix[j]-prefix[i]) %k =0 so in math prefix_i % k = prefix_j %k
            if remainder in mp:
                ans += mp[remainder]

            mp[remainder] = mp.get(remainder, 0) + 1

        return ans
