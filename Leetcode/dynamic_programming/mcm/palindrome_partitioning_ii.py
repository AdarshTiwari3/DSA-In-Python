import math

# v.v.v.imp


# Recursive Solution
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # recursive solution of MCM

        def is_palin(left, right) -> bool:
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1

                else:
                    return False

            return True

        def helper(i, j) -> int:
            if i == j:
                return 0

            if is_palin(
                i, j
            ):  # if string is also a palindrome there is no need to partition it
                return 0

            min_cut = math.inf
            for k in range(i, j):
                cut = helper(i, k) + helper(k + 1, j) + 1
                min_cut = min(min_cut, cut)

            return min_cut

        return helper(0, n - 1)


# Memoized Solution


class SolutionMemo:
    def minCut(self, s: str) -> int:
        n = len(s)

        # recursive solution of MCM
        # changing variables are i and j so memo array will be memo[n+1][n+1]
        memo = [[-1] * (n + 1) for _ in range(n + 1)]

        def is_palin(left, right) -> bool:
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1

                else:
                    return False

            return True

        def helper(i, j) -> int:
            if i == j:
                return 0

            if is_palin(
                i, j
            ):  # if string is also a palindrome there is no need to partition it
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            min_cut = math.inf
            for k in range(i, j):
                cut = helper(i, k) + helper(k + 1, j) + 1
                min_cut = min(min_cut, cut)

            memo[i][j] = min_cut

            return min_cut

        return helper(0, n - 1)


# more optimization on memoization, here we calculate the left and right partition also and store and check it inside memo array


class SolutionMemo2:
    def minCut(self, s: str) -> int:
        n = len(s)

        # recursive solution of MCM
        # changing variables are i and j so memo array will be memo[n+1][n+1]
        memo = [[-1] * (n + 1) for _ in range(n + 1)]

        def is_palin(left, right) -> bool:
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1

                else:
                    return False

            return True

        def helper(i, j) -> int:
            if i == j:
                return 0

            if is_palin(
                i, j
            ):  # if string is also a palindrome there is no need to partition it
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            min_cut = math.inf
            for k in range(i, j):
                left, right = 0, 0
                if (
                    memo[i][k] != -1
                ):  # left part is solved then check in memo array use it instead again calculation
                    left = memo[i][k]

                else:
                    left = helper(i, k)
                    memo[i][k] = left

                if (
                    memo[k + 1][j] != -1
                ):  # right part is solved then check in memo array use it instead again calculation
                    right = memo[k + 1][j]

                else:
                    right = helper(k + 1, j)
                    memo[k + 1][j] = right

                cut = left + right + 1
                min_cut = min(min_cut, cut)

            memo[i][j] = min_cut

            return min_cut

        return helper(0, n - 1)


# using front partition pattern


class SolutionFrontPartitionRecur:
    def minCut(self, s: str) -> int:
        n = len(s)

        def is_palin(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def helper(i):
            if i == n:
                return 0

            min_cut = math.inf

            for k in range(i, n):
                if is_palin(i, k):
                    cut = 1 + helper(k + 1)
                    min_cut = min(min_cut, cut)

            return min_cut

        return helper(0) - 1  # counted an extra partition after ending the last index


# so here changing variable is just i so take memo of size n+1


class SolutionFPMemo:
    def minCut(self, s: str) -> int:
        n = len(s)
        # so here changing variable is just i so take memo of size n+1
        memo = [-1] * (n + 1)

        def is_palin(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def helper(i):
            if i == n:
                return 0

            if memo[i] != -1:
                return memo[i]

            min_cut = math.inf

            for k in range(i, n):
                if is_palin(i, k):
                    cut = 1 + helper(k + 1)
                    min_cut = min(min_cut, cut)

            memo[i] = min_cut

            return min_cut

        return helper(0) - 1  # counted an extra partition after ending the last index


# TC => O(nxnxn) so this is still not an optimal solution because n = 2000 given which means it will be around 10^9 so TLE will be thrown here we have to optimize this in O(n x n) so calculation will be in 10^6 means accepted solution
# SC => O(n) # recursion space


# using palindromic dp concept TC=>O(n x n)


class SolutionDP:
    def minCut(self, s: str) -> int:
        n = len(s)
        # so here changing variable is just i so take memo of size n+1
        memo = [-1] * (n + 1)

        # here we made the palindromic substring dp using concept of palindromic substring
        palin_dp = [[False] * n for _ in range(n)]

        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (
                    end - start <= 2
                    or palin_dp[start + 1][
                        end - 1
                    ]  # here end - start <=2 manage 1 char 2 char and if any odd char in mid but still ends are palindrome so whole forms a palindrome
                ):
                    palin_dp[start][end] = True

        def helper(i):
            if i == n:
                return 0

            if memo[i] != -1:
                return memo[i]

            min_cut = math.inf

            for k in range(i, n):
                if palin_dp[i][k]:
                    cut = 1 + helper(k + 1)
                    min_cut = min(min_cut, cut)

            memo[i] = min_cut

            return min_cut

        return helper(0) - 1  # counted an extra partition after ending the last index


# O(n²)   (palindrome DP)
# +
# O(n²)   (front partition DP)
# =
# TC=> O(2n²) or O(n x n)
