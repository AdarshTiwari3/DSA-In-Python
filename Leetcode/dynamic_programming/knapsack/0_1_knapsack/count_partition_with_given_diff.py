# Count the number of subset with a given diff

# Recursive Solution


class SolutionRec:
    def countPartitions(self, arr, diff):
        # code here

        # lets directly implement recursive solution

        total_sum = sum(arr)
        if (total_sum - diff) % 2 == 1 or total_sum - diff < 0:
            return 0

        target = (total_sum - diff) // 2

        def helper(ind, target):
            if ind == len(arr):
                if target == 0:
                    return 1

                else:
                    return 0

            take = 0

            if arr[ind] <= target:
                take = helper(ind + 1, target - arr[ind])

            not_take = helper(ind + 1, target)

            return take + not_take

        return helper(0, target)


# TC= 2^n SC=O(n)

# Memoization Solution


class SolutionMemo:
    def countPartitions(self, arr, diff):
        # code here

        # lets directly implement memoization solution

        total_sum = sum(arr)
        if (total_sum - diff) % 2 == 1 or total_sum - diff < 0:
            return 0

        target = (total_sum - diff) // 2
        dp = [[-1 for _ in range(target + 1)] for _ in range(len(arr) + 1)]

        def helper(ind, target):
            if ind == len(arr):
                if target == 0:
                    return 1

                else:
                    return 0

            if dp[ind][target] != -1:
                return dp[ind][target]
            take = 0

            if arr[ind] <= target:
                take = helper(ind + 1, target - arr[ind])

            not_take = helper(ind + 1, target)

            dp[ind][target] = take + not_take

            return dp[ind][target]

        return helper(0, target)


# TC= O( n x target) SC= O( n x target) + O(n)


# 2D DP Solution


class SolutionDP:
    def countPartitions(self, arr, diff):
        # code here

        # lets directly implement 2D DP Solution - tabulation
        total_sum = sum(arr)
        if (total_sum - diff) % 2 == 1 or total_sum - diff < 0:
            return 0

        target = (total_sum - diff) // 2

        dp = [[0 for _ in range(target + 1)] for _ in range(len(arr) + 1)]

        dp[0][0] = 1

        for i in range(1, len(arr) + 1):
            for j in range(target + 1):
                pick = 0

                if (
                    arr[i - 1] <= j
                ):  # i-1 because the actual index starts from 1st as 0th was used in initialization
                    pick = dp[i - 1][j - arr[i - 1]]

                not_pick = dp[i - 1][j]
                dp[i][j] = pick + not_pick

        return dp[len(arr)][target]


sol_dp = SolutionDP()
ans = sol_dp.countPartitions([1, 1, 2, 3], 1)
print("ans=", ans)

# TC- O(n x target) SC= O(n x target)

# 1-D DP Solution


class Solution:
    def countPartitions(self, arr, diff):
        # code here

        # lets directly implement 1D DP Solution
        total_sum = sum(arr)

        if (total_sum - diff) % 2 == 1 or total_sum - diff < 0:
            # partition not possible
            return 0

        target = (total_sum - diff) // 2

        dp = [0] * (target + 1)
        dp[0] = 1  # base case

        for i in range(len(arr)):
            for j in range(target, arr[i] - 1, -1):
                dp[j] = dp[j] + dp[j - arr[i]]

        return dp[target]


sol = Solution()
ans = sol.countPartitions([1, 1, 2, 3], 1)
print("ans=", ans)

ans = sol.countPartitions([1, 1, 2, 3], 12)
print("ans=", ans)

ans1 = sol.countPartitions([1, 3, 3, 2, 1], 5)
print("ans=", ans1)


# TC= O(n*target) SC=O(target)
