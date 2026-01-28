# recursion Solution

# the intent of this question is diff from choin change 1 , here we want to get the possible ways to get the amount using coins
# in coin change we wanted to get the number of possible coins - means selection
from typing import List


class SolutionRecur:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        def helper(ind, capacity):
            if capacity == 0:
                return 1

            if ind < 0:
                return 0

            take = 0

            if coins[ind] <= capacity:
                take = helper(ind, capacity - coins[ind])
            not_take = helper(ind - 1, capacity)

            return take + not_take

        return helper(n - 1, amount)


sol = SolutionRecur()
coins = [1, 2, 5]
amount = 5
ans = sol.change(amount, coins)
print("ans_recur=", ans)  # 4


# Memoized Solution
class SolutionMemo:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        memo = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]

        def helper(ind, capacity):
            if capacity == 0:
                return 1

            if ind < 0:
                return 0

            if memo[ind][capacity] != -1:
                return memo[ind][capacity]

            take = 0

            if coins[ind] <= capacity:
                take = helper(ind, capacity - coins[ind])
            not_take = helper(ind - 1, capacity)

            memo[ind][capacity] = take + not_take

            return memo[ind][capacity]

        return helper(n - 1, amount)


sol_memo = SolutionMemo()
coins = [1, 2, 5]
amount = 5
ans_memo = sol_memo.change(amount, coins)
print("ans_memo=", ans_memo)  # 4
