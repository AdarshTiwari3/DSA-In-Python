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

# TC=> O(2^(n + amount)) SC=> O(amount) because selection is based on amount


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
