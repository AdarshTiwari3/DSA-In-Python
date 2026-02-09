class Solution:
    def longestPalindrome(self, s: str) -> str:
        # reverse the first string and find the longest common substring
        # longest common substring will be similar to lcs just only when string order breaks then count become 0
        # get the last index of substring where it broke and return end index to max length of the substring

        n = len(s)
        s2 = s[::-1]

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        max_len = 0
        end = 0

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                    start = i - dp[i][j]

                    mirror = n - j

                    if start == mirror:
                        if dp[i][j] > max_len:
                            max_len = dp[i][j]
                            end = i
                else:
                    dp[i][j] = 0

        return s[end - max_len : end]  # this ensures starting of the substring to end
