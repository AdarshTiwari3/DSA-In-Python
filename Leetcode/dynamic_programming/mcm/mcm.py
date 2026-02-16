import math


# Recursive Solution
class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)

        def helper(i, j):
            if i >= j:
                return 0

            min_cost = math.inf

            for k in range(i, j):
                total_cost = (
                    helper(i, k) + helper(k + 1, j) + arr[i - 1] * arr[k] * arr[j]
                )

                min_cost = min(min_cost, total_cost)

            return min_cost

        return helper(
            1, n - 1
        )  # here i will start from 1 because 0 can't form the matrix the formula will be Ai=arr[i-1] x arr[i]


sol = Solution()
arr = [10, 30, 5, 60]
ans = sol.matrixMultiplication(arr)

print("ans_rec=", ans)  # 4500

# TC=> O(2^n) SC=> O(n)


# Memoized Solution


class SolutionMemo:
    def matrixMultiplication(self, arr):
        n = len(arr)
        memo = [[-1] * (n + 1) for _ in range(n + 1)]

        def helper(i, j):
            if i >= j:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            min_cost = math.inf

            for k in range(i, j):
                total_cost = (
                    helper(i, k) + helper(k + 1, j) + arr[i - 1] * arr[k] * arr[j]
                )

                min_cost = min(min_cost, total_cost)
            memo[i][j] = min_cost

            return min_cost

        return helper(1, n - 1)


sol = SolutionMemo()
arr = [10, 30, 5, 60]
ans = sol.matrixMultiplication(arr)

print("ans_rec=", ans)  # 4500

# TC => O(n x n x n) # extra n is for loop
# SC => O(n x n) + O(n) , n x n for memo table and extra n for recursion
