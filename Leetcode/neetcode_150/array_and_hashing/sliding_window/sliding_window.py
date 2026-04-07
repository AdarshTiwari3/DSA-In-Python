"""Sliding Window Implementation"""


class SlidingWindow:
    # fixed size window
    def implementSlidingWindow(self, arr, k) -> int:
        window_sum = 0
        ans = 0

        for i, num in enumerate(arr):
            window_sum += num

            if i >= k - 1:  # because i is following 0 based indexing
                ans = max(ans, window_sum)
                window_sum -= arr[i - k + 1]  # this always shrinks the value from left

        return ans


sol = SlidingWindow()
arr = [100, 200, 300, 400, 500]
k = 2
ans = sol.implementSlidingWindow(arr=arr, k=k)

print("ans=", ans)

# TC=> O(n)
# SC=> O(1)
