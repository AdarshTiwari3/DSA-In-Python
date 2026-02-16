# Two Pointers


class Solution:
    def countSubstrings(self, s: str) -> int:
        # here we will consider that we are at the middle and moving left and right to check the palindrome for each index but here is a catch
        # there will be odd and even check 1, 3,5 and 2, 4 and 6

        n = len(s)
        self.ans = 0

        def helper(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                self.ans += 1
                left -= 1
                right += 1

        for i in range(n):
            helper(i, i)  # odd check initially i=j 0,0 and start moving
            helper(i, i + 1)

        return self.ans


sol = Solution()
ans = sol.countSubstrings("aaab")
print("ans=", ans)
# TC=> O(n x n)
# SC=> O(1)


class SolutionMemo:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # -1 = not computed
        #  0 = not palindrome
        #  1 = palindrome
        memo = [[-1] * (n + 1) for _ in range(n + 1)]

        def isPal(start, end):
            if start >= end:
                return 1  # True

            if memo[start][end] != -1:
                return memo[start][end]

            if s[start] != s[end]:
                memo[start][end] = 0
            else:
                memo[start][end] = isPal(
                    start + 1, end - 1
                )  # check on smaller substring

            return memo[start][end]

        count = 0
        for start in range(n):
            for end in range(start, n):
                if isPal(start, end) == 1:
                    count += 1

        return count


sol = Solution()
ans = sol.countSubstrings("aaab")
print("ans_memo=", ans)

# TC=> O(n x n)
# SC=> O(n x n) + O(n)


# DP Solution


class SolutionDP:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [
            [False] * (n + 1) for _ in range(n + 1)
        ]  # why bool array? because each says whether it is Palindrome or not
        ans = 0

        for end in range(1, n + 1):  # right boundary
            for start in range(end, 0, -1):  # left boundary
                if s[start - 1] == s[end - 1]:
                    if (
                        end - start <= 2
                    ):  # this handles the 1 len, 2 len and single inner string case
                        dp[start][end] = True
                    else:
                        dp[start][end] = dp[start + 1][
                            end - 1
                        ]  # this checks the inner string means if current check is start = a and end =a it will check the inner content whether it is also a palindrome or not

                if dp[start][end]:
                    ans += 1
        return ans


sol = SolutionDP()
ans = sol.countSubstrings("aaab")
print("ans_dp=", ans)

# TC=> O(n x n)
# SC=> O(n x n)
