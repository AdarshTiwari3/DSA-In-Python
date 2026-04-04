from typing import List


class Solution:
    def suffixSum(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        n = len(arr)

        suffix = [0] * n

        suffix[n - 1] = arr[n - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + arr[i]

        return suffix


sol = Solution()
arr = [3, 7, 1, 8, 10]
suffix_sum = sol.suffixSum(arr=arr)

print("suffix_sum=", suffix_sum)  # [29, 26, 19, 18, 10]


# TC=> O(n)
# SC=> O(n)
