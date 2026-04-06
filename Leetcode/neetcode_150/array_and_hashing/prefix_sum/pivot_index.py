from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        suffix = [0] * n
        suffix[n - 1] = nums[n - 1]  # right array suffix sum
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        left = 0
        for i in range(n):
            if suffix[i] - nums[i] == left:
                return i
            left += nums[i]

        return -1


# TC=> O(n)
# SC=> O(n)


class SolutionOptimal:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for i, num in enumerate(nums):
            right = total - left - num
            if left == right:
                return i
            left += num

        return -1


# TC=> O(n)
# SC=> O(1)
