# Recursive solution with memo


class SolutionMemo:
    def longestPalinSubseq(self, s):
        # code here

        # reverse the s and give name s2 and then find the lcs of both that will be the longest palindromic seq
        s2 = s[::-1]
        n = len(s)
        memo = [[-1] * (n + 1) for _ in range(n + 1)]

        def helper(i, j):
            if i == 0 or j == 0:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            if s[i - 1] == s2[j - 1]:
                memo[i][j] = 1 + helper(i - 1, j - 1)
            else:
                memo[i][j] = max(helper(i - 1, j), helper(i, j - 1))
            return memo[i][j]

        return helper(n, n)


sol_memo = SolutionMemo()
s = "axbcba"
ans_memo = sol_memo.longestPalinSubseq(s)

print("ans_memo=", ans_memo)  # 5- abcba


class SolutionDP:
    def longestPalindromeSubseq(self, s: str) -> int:
        # reverse the first string and give a name s2 then find the lcs of both
        s2 = s[::-1]

        n = len(s)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # the lcs length will be the longest palidromic sub
        return dp[n][n]


sol_dp = SolutionDP()
s = "agbcba"
ans_dp = sol_dp.longestPalindromeSubseq(s)
print("ans_dp=", ans_dp)  # 5
