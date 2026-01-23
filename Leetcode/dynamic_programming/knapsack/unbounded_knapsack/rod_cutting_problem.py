from typing import List


# normal recursion solution
class SolutionRecursion:
    def canRod(self, price: List[int]) -> int:
        n = len(price)

        def helper(rodLen, capacity):
            if capacity == 0:
                return 0

            if rodLen == 1:
                possible_times = capacity // rodLen
                return possible_times * price[0]

            take = 0

            if rodLen <= capacity:
                # legal move
                take = price[rodLen - 1] + helper(rodLen, capacity - rodLen)

            not_take = helper(rodLen - 1, capacity)

            return max(take, not_take)

        return helper(n, n)


sol = SolutionRecursion()
price = [3, 5, 8, 9, 10, 17, 17, 20]
ansRec = sol.canRod(price)
print("ans_recur=", ansRec)

# TC=> O(2^n) SC=> O(n)


# Memoization Solution
class SolutionMemo:
    def cutRod(self, price: List[int]) -> int:
        n = len(price)
        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        def helper(rodLen, capacity):

            if capacity == 0:
                return 0

            if rodLen == 1:
                possible_times = capacity // rodLen
                return possible_times * price[0]

            if dp[rodLen][capacity] != -1:
                return dp[rodLen][capacity]

            take = 0

            if rodLen <= capacity:
                take = price[rodLen - 1] + helper(rodLen, capacity - rodLen)

            not_take = helper(rodLen - 1, capacity)

            dp[rodLen][capacity] = max(take, not_take)

            return dp[rodLen][capacity]

        return helper(n, n)


sol_memo = SolutionMemo()
price = [3, 5, 8, 9, 10, 17, 17, 20]
ans_memo = sol_memo.cutRod(price)
print("ans_memo=", ans_memo)

# TC=> O(n x n) SC=> O(n x n) + O(n)

# Tabulation Solution


class Solution:
    def cutRod(self, price: List[int]) -> int:
        n = len(price)

        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(n + 1):
                take = 0
                if i <= j:
                    take = price[i - 1] + dp[i][j - i]
                not_take = dp[i - 1][j]
                dp[i][j] = max(take, not_take)

        return dp[n][n]


sol_tab = Solution()
price = [1, 5, 8, 9, 10, 17, 17, 20]
ans_tab = sol_tab.cutRod(price)
print("ans_tab=", ans_tab)

# TC=> O(n x n) SC=> O(n x n)


# 1-D DP Solution
class Solution:
    def cutRod(self, price: List[int]) -> int:
        n = len(price)

        dp = [0] * (n + 1)

        for i in range(
            1, n + 1
        ):  # because i represents the length of a rod which i so it should be started from 1
            for j in range(i, n + 1):  # why j? to avoid j<i condition
                # price array starts from 0
                dp[j] = max(
                    dp[j], price[i - 1] + dp[j - i]
                )  # why j-i --> Remaining rod length if we consider j as total size and i as current size

        return dp[n]


sol = Solution()
price = [1, 5, 8, 9, 10, 17, 17, 20]
ans = sol.cutRod(price)

print("ans_dp=", ans)  # 22
