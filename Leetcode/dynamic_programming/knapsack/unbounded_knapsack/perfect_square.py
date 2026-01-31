import math


class Solution:
    def numSquares(self, n: int) -> int:
        # lets solve this using recursion
        # first we will see what are the possible perfect squares for given number
        # suppose for n =12 we can have 1, 4, 9 only so this will be our recursion options

        def helper(n):
            if n == 0:
                return 0

            ans = math.inf

            i = 1

            # check the under roots possible

            while i * i <= n:
                ans = min(ans, 1 + helper(n - i * i))
                i += 1

            return ans

        return helper(n)


sol = Solution()
ans = sol.numSquares(12)

print("ans_recur=", ans)  # 3 => 4+4+4

# TC=>O(kⁿ) or exponential ( k = under root ) SC=> O(n)


class SolutionMemo:
    def numSquares(self, n: int) -> int:
        # lets solve this using recursion
        # first we will see what are the possible perfect squares for given number
        # suppose for n =12 we can have 1, 4, 9 only so this will be our recursion options
        # memoized solution

        memo = [-1] * (n + 1)

        def helper(n):
            if n == 0:
                return 0

            if memo[n] != -1:
                return memo[n]

            ans = math.inf

            i = 1

            # check the under roots possible

            while i * i <= n:
                ans = min(ans, 1 + helper(n - i * i))
                i += 1
            memo[n] = ans
            return memo[n]

        return helper(n)


sol_memo = SolutionMemo()
ans_memo = sol_memo.numSquares(12)

print("ans_memo=", ans_memo)  # 3 => 4+4+4

# TC = O(n √n) SC=>O(n)
