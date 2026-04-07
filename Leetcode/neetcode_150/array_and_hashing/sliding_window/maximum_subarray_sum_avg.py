from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0

        ans = -float("inf")

        for i, num in enumerate(nums):
            window_sum += num

            if i >= k - 1:

                ans = max(ans, window_sum)

                # shrink from left window

                window_sum -= nums[i - k + 1]

        return ans / k  # max sum will have max avg
