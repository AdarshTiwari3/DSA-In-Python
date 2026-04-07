class Solution:
    def maxSubarraySum(self, arr, k):
        # code here

        # use sliding window

        window_sum = 0
        ans = 0

        for i, num in enumerate(arr):
            window_sum += num

            if i >= k - 1:
                ans = max(ans, window_sum)
                # shrink from left
                window_sum -= arr[i - k + 1]  # +1 to avoid negative indexes

        return ans
