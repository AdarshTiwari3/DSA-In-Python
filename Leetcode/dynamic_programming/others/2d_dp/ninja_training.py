class Solution:
    def maximumPoints(self, mat):
        # code here

        n = len(mat)

        def helper(day, last_day):
            if day == n:
                return 0

            ans = 0

            for activity in range(3):
                if activity != last_day:
                    curr_point = mat[day][activity] + helper(day + 1, activity)
                    ans = max(ans, curr_point)

            return ans

        return helper(0, -1)


# TC = O(3^n) # because we 3 choices
# SC = O(n)


class SolutionMemo:
    def maximumPoints(self, mat):
        # code here

        n = len(mat)
        # here as the changin variables are day and last day so we can take the memo array of n+1, n+1 size

        memo = [[-1] * (4) for _ in range(n + 1)]

        def helper(day, last_day):
            if day == n:
                return 0

            if memo[day][last_day] != -1:
                return memo[day][last_day]

            ans = 0

            for activity in range(3):
                if activity != last_day:
                    curr_point = mat[day][activity] + helper(day + 1, activity)
                    ans = max(ans, curr_point)

            memo[day][last_day] = ans
            return ans

        return helper(0, 3)


# TC = O(n × 4 × 3) # 3 activity, running, fighting and learning and 4 is here possibility of last working day index, one is 0,1,2,3,
# SC= O(n x 4) = O(n) + O(n) for recursion


class SolutionTabulation:
    def maximumPoints(self, mat):
        # code here

        n = len(mat)
        # here as the changin variables are day and last day so we can take the memo array of n+1, n+1 size

        dp = [[0] * (4) for _ in range(n + 1)]

        for day in range(1, n + 1):
            for last in range(4):
                best = 0
                for activity in range(3):
                    if last != activity:
                        points = mat[day - 1][activity] + dp[day - 1][activity]
                        best = max(best, points)

                dp[day][last] = best

        return dp[n][3]


# TC=> O(n)
# SC=> O(n)
