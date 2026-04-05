from typing import List


class Solution:
    def prefixSum(self, arr: List[int]) -> List[int]:
        prefix = [0] * len(arr)
        prefix[0] = arr[0]

        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] + arr[i]

        return prefix


sol = Solution()
arr = [3, 7, 1, 8, 10]
prefix_sum = sol.prefixSum(arr=arr)

print("prefix_sum=", prefix_sum)  # [3, 10, 11, 19, 29]


# TC=> O(n)
# SC=> O(n)
