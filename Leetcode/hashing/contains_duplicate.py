from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        vis = set()

        for num in nums:
            if num in vis:
                return True

            vis.add(num)

        return False


class SolutionDict:
    def containsDuplicate(self, nums: List[int]) -> bool:

        n = len(nums)

        freq = {}

        for i in range(n):
            if nums[i] in freq:
                return True

            freq[nums[i]] = 1

        return False


class SolutionSetLen:
    def containsDuplicate(self, nums: List[int]) -> bool:

        n = len(nums)

        num_set = set(nums)

        if len(num_set) < n:
            return True

        return False


"""
TC=> O(n)
SC=> O(n)

best case can be O(1) in first solution of set and dict

"""
