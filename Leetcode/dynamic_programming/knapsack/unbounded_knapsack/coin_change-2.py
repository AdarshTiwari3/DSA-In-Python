# recursion Solution

# the intent of this question is diff from choin change 1 , here we want to get the possible ways to get the amount using coins
# in coin change we wanted to get the number of possible coins - means selection
from typing import List


class SolutionRecur:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        def helper(ind, amount):
            if amount == 0:
                return 1

            # if ind == 0:
            #     if amount % coins[0] == 0:
            #         return 1
            #     else:
            #         return 0
            if ind < 0:
                return 0

            take = 0

            if coins[ind] <= amount:
                take = helper(ind, amount - coins[ind])
            not_take = helper(ind - 1, amount)

            return take + not_take

        return helper(n - 1, amount)


sol = SolutionRecur()
coins = [1, 2, 5]
amount = 5
ans = sol.change(amount, coins)
print("ans_recur=", ans)  # 4

# TC=> O(2^(amount)) SC=>O(amount)


# Memoized Solution
class SolutionMemo:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        memo = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]

        def helper(ind, amount):
            if amount == 0:
                return 1

            if ind < 0:
                return 0

            if memo[ind][amount] != -1:
                return memo[ind][amount]

            take = 0

            if coins[ind] <= amount:
                take = helper(ind, amount - coins[ind])
            not_take = helper(ind - 1, amount)

            memo[ind][amount] = take + not_take

            return memo[ind][amount]

        return helper(n - 1, amount)


sol_memo = SolutionMemo()
coins = [1, 2, 5]
amount = 5
ans_memo = sol_memo.change(amount, coins)
print("ans_memo=", ans_memo)  # 4

# TC=> O(n x amount) SC=> O(n x amount) + O(n)


# tabulation solution - 2D DP


class SolutionTab:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1  # first column will be 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                take = 0

                if coins[i - 1] <= j:
                    take = dp[i][j - coins[i - 1]]

                not_take = dp[i - 1][j]

                dp[i][j] = take + not_take

        return dp[n][amount]


sol_tab = SolutionTab()
coins = [1, 2, 5]
amount = 5
ans_tab = sol_tab.change(amount, coins)
print("ans_tab=", ans_tab)  # 4

# TC=> O(n x amount) SC=> O(n x amount)
