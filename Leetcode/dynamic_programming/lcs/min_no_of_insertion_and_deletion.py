class Solution:
    def minOperations(self, s1, s2):
        n = len(s1)
        m = len(s2)

        memo = [[-1] * (m + 1) for _ in range(n + 1)]

        def helper(i, j):
            if i == 0 or j == 0:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            if s1[i - 1] == s2[j - 1]:
                memo[i][j] = 1 + helper(i - 1, j - 1)
            else:
                memo[i][j] = max(helper(i - 1, j), helper(i, j - 1))

            return memo[i][j]

        lcs_len = helper(n, m)
        return (n - lcs_len) + (m - lcs_len)


sol_memo = Solution()
s1 = "heap"
s2 = "pea"
ans_memo = sol_memo.minOperations(s1, s2)
print("ans_memo=", ans_memo)  # 3

# TC => O(n × m) SC=> O(n * m) + O(n + m)


# User function Template for python3
class SolutionTab:
    def minOperations(self, s1, s2):
        # code here

        # find the common string which is LCS and then minus this from n and m

        n = len(s1)
        m = len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lcs_len = dp[n][m]
        return n - lcs_len + m - lcs_len


sol_tab = SolutionTab()
s1 = "geeksforgeeks"
s2 = "geeks"
ans_tab = sol_tab.minOperations(s1, s2)
print("ans_tab=", ans_tab)  # 8

# TC => O(n × m) SC=> O(n * m)
