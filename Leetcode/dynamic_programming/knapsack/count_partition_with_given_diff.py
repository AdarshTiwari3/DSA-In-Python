# Count the number of subset with a given diff


class Solution:
    def countPartitions(self, arr, diff):
        # code here

        # lets directly implement 1D DP Solution
        total_sum = sum(arr)

        if (total_sum - diff) % 2 == 1 or total_sum - diff < 0:
            # partition not possible
            return 0

        target = (total_sum - diff) // 2

        dp = [0] * (target + 1)
        dp[0] = 1  # base case

        for i in range(len(arr)):
            for j in range(target, arr[i] - 1, -1):
                dp[j] = dp[j] + dp[j - arr[i]]

        return dp[target]


sol = Solution()
ans = sol.countPartitions([1, 1, 2, 3], 1)
print("ans=", ans)

ans = sol.countPartitions([1, 1, 2, 3], 12)
print("ans=", ans)

ans1 = sol.countPartitions([1, 3, 3, 2, 1], 5)
print("ans=", ans1)
