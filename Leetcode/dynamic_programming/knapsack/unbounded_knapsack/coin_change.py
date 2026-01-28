import math
from typing import List


# recursive solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        def helper(ind, capacity):
            if capacity == 0:
                return 0

            if ind == 0:
                if capacity % coins[0] != 0:
                    return math.inf  # not possible
                return capacity // coins[0]

            take = math.inf

            if coins[ind] <= capacity:
                take = 1 + helper(ind, capacity - coins[ind])

            not_take = helper(ind - 1, capacity)

            return min(take, not_take)

        ans = helper(n - 1, amount)

        return ans if ans != math.inf else -1


sol = Solution()
coins = [1, 2, 5]
amount = 11
ans = sol.coinChange(coins, amount)

print("ans_recur=", ans)  # 3

# TC=> O(2^(amount)) SC=> O(amount) because selection is based on amount


# Memoized Solution


class SolutionMemo:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        memo = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]

        def helper(ind, capacity):
            if capacity == 0:
                return 0

            if ind == 0:
                if capacity % coins[0] != 0:
                    return math.inf  # not possible
                return capacity // coins[0]

            if memo[ind][capacity] != -1:
                return memo[ind][capacity]

            take = math.inf

            if coins[ind] <= capacity:
                take = 1 + helper(ind, capacity - coins[ind])

            not_take = helper(ind - 1, capacity)

            memo[ind][capacity] = min(take, not_take)
            return memo[ind][capacity]

        ans = helper(n - 1, amount)

        return (
            ans if ans != math.inf else -1
        )  # check after result if not possible return -1


sol_memo = SolutionMemo()
coins = [2, 5, 10, 1]
amount = 27
ans_memo = sol_memo.coinChange(coins, amount)
print("ans_memo=", ans_memo)  # 4

# TC=> O(n x amount) SC=>O(n x amount) + O(amount)


# tabulation solution - 2D dp
class SolutionTab:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # tabulation solution 2D - dp

        dp = [[math.inf for _ in range(amount + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                take = math.inf
                if coins[i - 1] <= j:
                    take = 1 + dp[i][j - coins[i - 1]]
                not_take = dp[i - 1][j]

                dp[i][j] = min(take, not_take)

        return dp[n][amount] if dp[n][amount] != math.inf else -1


sol_tab = SolutionTab()
coins = [2, 5, 10, 1]
amount = 27
ans_tab = sol_tab.coinChange(coins, amount)
print("ans_tab=", ans_tab)  # 4

# TC=> O(n x amount) SC=>O(n x amount)


# 1-d DP Solution


class SolutionDP:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # tabulation solution 1D - dp

        dp = [math.inf] * (amount + 1)

        dp[0] = 0

        for i in range(n):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j], 1 + dp[j - coins[i]])

        return dp[amount] if dp[amount] != math.inf else -1


sol_dp = SolutionDP()
coins = [2, 5, 10, 1]
amount = 27
ans_dp = sol_dp.coinChange(coins, amount)
print("ans_dp=", ans_dp)  # 4

# TC=> O(n x amount) SC=>O(amount)
