"""LCS Implementation"""


# recursion solution
class LCSRecur:
    def solveLcs(self, x: str, y: str, n: int, m: int) -> int:
        def helper(x: str, y: str, n: int, m: int) -> int:
            if (
                n == 0 or m == 0
            ):  # base case if any string is empty then lcs is not possible
                return 0

            # case 1 if last index of both string matches

            if x[n - 1] == y[m - 1]:
                # take so 1+
                return 1 + helper(x, y, n - 1, m - 1)

            else:
                # take the max of both (n , m-1) and (n-1, m)
                return max(helper(x, y, n, m - 1), helper(x, y, n - 1, m))

        return helper(x, y, n, m)


sol_recur = LCSRecur()
x = "abcdgh"
y = "abedfhr"
n = len(x)
m = len(y)
ans = sol_recur.solveLcs(x, y, n, m)

print("ans_recur=", ans)  # 4 => abdh


# TC ≈ O(2^(n + m)) SC=> O(n + m)

# Memoized Solution
# Changing variables are n and m so memo array will be formed using this only


class LCSMemo:
    def solveLcs(self, x: str, y: str, n: int, m: int) -> int:
        memo = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

        def helper(x: str, y: str, n: int, m: int) -> int:
            if (
                n == 0 or m == 0
            ):  # base case if any string is empty then lcs is not possible
                return 0

            # check if values are present in memoized/dp array
            if memo[n][m] != -1:
                return memo[n][m]
            # case 1 if last index of both string matches

            if x[n - 1] == y[m - 1]:
                # take so 1+
                memo[n][m] = 1 + helper(x, y, n - 1, m - 1)
                return memo[n][m]

            else:
                # take the max of both (n , m-1) and (n-1, m)
                memo[n][m] = max(helper(x, y, n, m - 1), helper(x, y, n - 1, m))
                return memo[n][m]

        return helper(x, y, n, m)


sol_memo = LCSMemo()
ans_memo = sol_memo.solveLcs(x, y, n, m)
print("ans_memo=", ans_memo)

# TC = O(n * m) SC = O(n * m)
