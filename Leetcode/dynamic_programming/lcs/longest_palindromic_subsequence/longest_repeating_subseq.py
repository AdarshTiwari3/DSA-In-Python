# User function Template for python3

#  i == j in not possibile because
# axxyx
# axxyx
"""
xx
xx
here repeatition is possible only 0th index of first string goes with 1st index of second string means cross only possible

or s= aabb
0 1 2 3
a a b b
a a b b

here 0 2 from first and 1 3 from second, lcs= ab
or 1 3 from first and 0 2 from second possible

"""


class Solution:
    def LongestRepeatingSubsequence(self, s):
        # Code here

        n = len(s)

        # find the LCS

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s[j - 1] and i != j:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][n]


# TC=> O(n x n) SC=>O(n x n)
