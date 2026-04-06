from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # using prefix and suffix product

        prefix, suffix, ans = [1] * n, [1] * n, []
        prefix[0] = 1

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        suffix[n - 1] = 1

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        ans = [0] * n

        for i in range(n):
            ans[i] = prefix[i] * suffix[i]

        return ans


# TC=> O(n)
# SC=> O(n)


class SolutionOptimal:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # prefix  product here prefix is left product of an index

        prefix, ans = [1] * n, [0] * n
        prefix[0] = 1

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        right = 1
        for i in range(n - 1, -1, -1):
            ans[i] = prefix[i] * right
            right *= nums[i]

        return ans


# TC => O(n)
# SC => O(n) # here we remove the extra space for suffix array


class SolutionMostOptimal:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # prefix  product currently we will use ans array itself for left product calculation

        ans = [1] * n

        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        right = 1
        for i in range(n - 1, -1, -1):
            ans[i] = ans[i] * right
            right *= nums[i]

        return ans


# TC => O(n)
# SC => O(1) # if we dont consider the ans array because it is already expectation so we have not used any extra space here
