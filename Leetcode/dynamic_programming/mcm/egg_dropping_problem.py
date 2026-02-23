# User function Template for python3
import math


class SolutionRecur:

    # Function to find minimum number of attempts needed in
    # order to find the critical floor.
    def eggDrop(self, n, k):
        # code here
        # here we have to find minimum in worst case
        # recursive solution using mcm dp concept of k partition range
        def helper(n, f):
            if f == 0 or f == 1:
                return f

            if n == 1:
                return f

            ans = math.inf

            for k in range(1, f + 1):  # check till last floor
                temp = 1 + max(
                    helper(n - 1, k - 1), helper(n, f - k)
                )  # break and not break in worst case
                ans = min(ans, temp)

            return ans

        return helper(n, k)


# Time Complexity  = O(2^f) here f is floor
# Space Complexity = O(f)

sol = SolutionRecur()
ans = sol.eggDrop(1, 36)
print("ans_recur=", ans)  # 36


# User function Template for python3


class SolutionMemo:

    # Function to find minimum number of attempts needed in
    # order to find the critical floor.
    def eggDrop(self, n, k):
        # code here
        # here we have to find minimum in worst case
        # recursive solution using mcm dp concept of k partition range
        # the changing variables are egg and floor so memo array will be memo[n+1][k+1]
        memo = [[-1] * (k + 1) for _ in range(n + 1)]

        def helper(n, f):
            if f == 0 or f == 1:
                return f

            if n == 1:
                return f

            if memo[n][f] != -1:
                return memo[n][f]

            ans = math.inf

            for k in range(1, f + 1):  # check till last floor
                temp = 1 + max(
                    helper(n - 1, k - 1), helper(n, f - k)
                )  # break and not break in worst case
                ans = min(ans, temp)

            memo[n][f] = ans
            return ans

        return helper(n, k)


sol = SolutionMemo()
ans = sol.eggDrop(2, 36)
print("ans_recur=", ans)  # 8
