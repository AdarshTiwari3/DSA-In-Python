from typing import List

# it is same question of count partition with given diff as if we see the array can be divided into two parts left represents with + values and right with - so here we check the possible subset count only with the formula of s1=(total_sum-diff)//2


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        if total_sum < target or (total_sum - target) % 2:
            return 0

        sum1 = (total_sum - target) // 2

        # directly using the 1D DP

        dp = [0] * (sum1 + 1)

        dp[0] = 1

        for i in range(len(nums)):
            for j in range(sum1, nums[i] - 1, -1):
                dp[j] = dp[j] + dp[j - nums[i]]

        return dp[sum1]


sol = Solution()
ans = sol.findTargetSumWays([1, 2, 1, 3], 1)
print("ans=", ans)

# TC: O( n x target) SC: O(target)
