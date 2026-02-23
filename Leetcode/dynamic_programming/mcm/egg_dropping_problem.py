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


# More optimization in calculation


class SolutionMemoOpti:

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
                # lets store break and not break into memo and explictly check it
                egg_break, egg_not_break = 0, 0
                if memo[n - 1][k - 1] != -1:
                    egg_break = memo[n - 1][k - 1]
                else:
                    egg_break = helper(n - 1, k - 1)
                    memo[n - 1][k - 1] = egg_break

                if memo[n][f - k] != -1:
                    egg_not_break = memo[n][f - k]
                else:
                    egg_not_break = helper(n, f - k)
                    memo[n][f - k] = egg_not_break

                temp = 1 + max(
                    egg_break, egg_not_break
                )  # break and not break in worst case
                ans = min(ans, temp)

            memo[n][f] = ans
            return ans

        return helper(n, k)


# using binary search


class SolutionMemoBinarySearch:

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
            low, high = 1, f
            # # using binary search instead of linear loop reduces time complexity per state from O(k) to O(log k)

            while low <= high:
                mid = (low + high) // 2
                # here k breakpoint will be mid

                egg_break = helper(n - 1, mid - 1)
                egg_not_break = helper(n, f - mid)  # new total floor will be f-k

                temp = 1 + max(egg_break, egg_not_break)
                ans = min(ans, temp)

                # move toward worst side
                if egg_break > egg_not_break:
                    # move downward
                    high = mid - 1  # becase mid already taken

                else:
                    # move low to mid+1, because mid already taken
                    low = mid + 1

            memo[n][f] = ans
            return ans

        return helper(n, k)


sol = SolutionMemoBinarySearch()
ans = sol.eggDrop(2, 36)
print("ans_recur=", ans)  # 8

# TC  = O(n × k log k) # n and k for subproblem state calculation and log k for binary search
# SC = O(n × k)
