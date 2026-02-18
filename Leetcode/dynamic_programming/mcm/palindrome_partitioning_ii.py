import math


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
