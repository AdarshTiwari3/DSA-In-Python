# Recursive solution of Scramble string


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        def helper(s1, s2) -> bool:
            # base cases
            if len(s1) != len(s2):
                return False  # not possible

            if s1 == s2:
                return True

            n = len(s1)

            for k in range(
                1, n
            ):  # k starts with 1 as atleast one is required and ends with n-1
                # case-1 swap possible
                # first part of s1 with second part of s2 and second part of s1 with first part of s2, substrings

                if helper(s1[:k], s2[n - k :]) and helper(s1[k:], s2[: n - k]):
                    return True

                # case -2 no swap
                # first part of s1 with first part of s2 and second part of s1 with second part of s2

                if helper(s1[:k], s2[:k]) and helper(s1[k:], s2[k:]):
                    return True

            return False

        return helper(s1, s2)


sol = Solution()
s1 = "great"
s2 = "rgeat"
ans = sol.isScramble(s1, s2)
print("ans_recur=", ans)  # True

# TC=> Exponential or O(2^n)
# SC=> O(n)


# Memoized Solution


class SolutionMemoMap:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = (
            {}
        )  # key: (s1, s2), value: True/False ---> using memo map to store substrings

        def helper(s1, s2) -> bool:
            # base cases
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            if len(s1) != len(s2):
                memo[(s1, s2)] = False
                return False  # not possible

            if s1 == s2:
                memo[(s1, s2)] = True
                return True

            n = len(s1)

            for k in range(
                1, n
            ):  # k starts with 1 as atleast one is required and ends with n-1
                # case-1 swap possible
                # first part of s1 with second part of s2 and second part of s1 with first part of s2, substrings

                if helper(s1[:k], s2[n - k :]) and helper(s1[k:], s2[: n - k]):
                    memo[(s1, s2)] = True
                    return True

                # case -2 no swap
                # first part of s1 with first part of s2 and second part of s1 with second part of s2

                if helper(s1[:k], s2[:k]) and helper(s1[k:], s2[k:]):
                    memo[(s1, s2)] = True
                    return True

            memo[(s1, s2)] = False
            return False

        return helper(s1, s2)


sol = SolutionMemoMap()
s1 = "great"
s2 = "rgeat"
ans = sol.isScramble(s1, s2)
print("ans_recur=", ans)  # True


# TC=> O(n^4)
# SC=> O(n ^ 3) + O(n)

# Using memoization with indices instead of substrings because substring slicing in Python takes O(n) time and O(n) space, which increases the overall time and space complexity. Using indices avoids creating new string objects and makes the solution more efficient.
# here we will be using the i, j and length the same substring approach but with these variables to avoid slicing hence the memo array will be the memo[n+1][n+1][n+1], because changing variables are i, j and length


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        # memo[i1][i2][length]- changing variables are i, j and length and with these indexes we are avoid the slicing approach which is too expensive in python

        memo = [
            [[-1 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)
        ]

        def helper(i, j, length) -> bool:
            # base cases

            if memo[i][j][length] != -1:
                return memo[i][j][length]

            if s1[i : i + length] == s2[j : j + length]:
                memo[i][j][length] = True
                return True

            for k in range(
                1, length
            ):  # k starts with 1 as atleast one is required and ends with n-1
                # case-1 swap possible
                # first part of s1 with second part of s2 and second part of s1 with first part of s2, substrings

                if helper(i, j + length - k, k) and helper(i + k, j, length - k):
                    memo[i][j][length] = True
                    return True

                # case -2 no swap
                # first part of s1 with first part of s2 and second part of s1 with second part of s2

                if helper(i, j, k) and helper(i + k, j + k, length - k):
                    memo[i][j][length] = True
                    return True

            memo[i][j][length] = False
            return False

        return helper(0, 0, n)  # here i and j are the starting index of s1, s2
