"""LCS Implementation"""


# recursion solution
def helper(x: str, y: str, n: int, m: int) -> int:
    if n == 0 or m == 0:  # base case if any string is empty then lcs is not possible
        return 0

    # case 1 if last index of both string matches

    if x[n - 1] == y[m - 1]:
        # take so 1+
        return 1 + helper(x, y, n - 1, m - 1)

    else:
        # take the max of both (n , m-1) and (n-1, m)
        return max(helper(x, y, n, m - 1), helper(x, y, n - 1, m))


x = "abcdgh"
y = "abedfhr"
n = len(x)
m = len(y)
ans = helper(x, y, n, m)

print("ans=", ans)  # 4 => abdh


# TC ≈ O(2^(n + m)) SC=> O(n + m)
