from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            curr_val = nums[left] + nums[right]
            if curr_val < target:
                left += 1
            elif curr_val > target:
                right -= 1

            else:
                return [left + 1, right + 1]

        return []


# TC=> O(n)
# SC=> O(1)
