from typing import List


class Solution:
    def unboundedKnapsack(self, W: int, wt: List[int], val: List[int]) -> int:
        n = len(wt)

        def helper(ind, capacity):
            """
            Generic base case (correct but slower):
            if capacity == 0 or ind < 0:
                return 0

            This version keeps recurring on index 0 and causes extra recursive calls.
            """

            if capacity == 0:
                return 0

            # optimized base case

            if ind == 0:
                # last element is left so why can't we get the max possible choices means if values at index is 2 and left capacity is 8 so we will go and pick 2 four times

                possible_times = capacity // wt[0]  # means example 8//2 =4

                return possible_times * val[0]

            pick = 0
            if wt[ind] <= capacity:
                pick = val[ind] + helper(ind, capacity - wt[ind])

            not_pick = helper(ind - 1, capacity)

            return max(pick, not_pick)

        return helper(n - 1, W)


sol = Solution()


wt = [5, 6, 7]
val = [10, 20, 30]
W = 3

ans = sol.unboundedKnapsack(W, wt, val)
print("ans=", ans)  # 0

wt = [2, 3]
val = [4, 5]
W = 7

ans = sol.unboundedKnapsack(W, wt, val)
print("ans=", ans)  # 13

wt = [3]
val = [10]
W = 9

ans = sol.unboundedKnapsack(W, wt, val)
print("ans=", ans)  # 30


# memoization solution

# the changing variables are capacity and n(size)


class SolutionMemo:
    def unboundedKnapsack(self, W: int, wt: List[int], val: List[int]) -> int:
        n = len(wt)

        dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]  # dp[N+1][W+1]

        def helper(ind, capacity):
            if capacity == 0:
                return 0

            if ind == 0:
                possible_count = capacity // wt[0]
                return possible_count * val[0]

            if dp[ind][capacity] != -1:
                return dp[ind][capacity]

            # take
            take = 0
            if wt[ind] <= capacity:
                take = val[ind] + helper(ind, capacity - wt[ind])

            not_take = helper(ind - 1, capacity)

            dp[ind][capacity] = max(take, not_take)

            return dp[ind][capacity]

        return helper(n - 1, W)


sol_memo = SolutionMemo()
wt = [2, 3]
val = [4, 5]
W = 7
ans_memo = sol_memo.unboundedKnapsack(W, wt, val)
print("ans_memo=", ans_memo)
# TC- O(n*W) SC- O(n*W) + O(n)


# DP Solution (Tabulation)


class SolutionTabulation:
    def unboundedKnapsack(self, W: int, wt: List[int], val: List[int]) -> int:
        n = len(wt)
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        print(dp)

        for i in range(1, n + 1):
            for j in range(1, W + 1):
                take = 0
                if wt[i - 1] <= j:
                    take = val[i - 1] + dp[i][j - wt[i - 1]]

                not_take = dp[i - 1][j]

                dp[i][j] = max(take, not_take)

        return dp[n][W]


sol_tab = SolutionTabulation()
wt = [2, 3]
val = [4, 5]
W = 7
ans_tab = sol_tab.unboundedKnapsack(W, wt, val)
print("ans_tab=", ans_tab)

# TC = O(n * W) SC= O(n * W)
