# V.V.V.Imp Question - Hard Problem


class SolutionRecur:
    def countWays(self, s):
        # code here
        # recursive solution
        n = len(s)

        def helper(i, j, is_true):
            if i > j:  # crossed the j so no possible ways
                return 0

            if i == j:
                if is_true:
                    # count the ways if it is true i.e "T" => 1
                    return 1 if s[i] == "T" else 0
                else:
                    # count the ways if it is False "F" => 1
                    return 1 if s[i] == "F" else 0

            ans = 0

            for k in range(i + 1, j, 2):

                # here we will calculate the true and false ways from left and right both side because the final ans depends on both side example if left is false and right is true then or of left, right comes true same vice versa

                leftTrue = helper(
                    i, k - 1, True
                )  # count total ways to get true for a given left expression, why k-1? because we want to get T/F string not operator
                leftFalse = helper(i, k - 1, False)
                rightTrue = helper(
                    k + 1, j, True
                )  # here again k+1 will be an operand means T/F string
                rightFalse = helper(k + 1, j, False)

                # check for the current operator |, &, ^, current index will be k

                if s[k] == "&":
                    if is_true:
                        # calculating for true
                        ans += (
                            leftTrue * rightTrue
                        )  # means if there are x ways to get true from left and y ways from right side then total ways will x*y because & checks for both true ways
                    else:
                        # calculating for False counts

                        ans += (
                            leftTrue * rightFalse
                            + leftFalse * rightTrue
                            + leftFalse * rightFalse
                        )

                elif s[k] == "|":
                    if is_true:
                        ans += (
                            leftTrue * rightFalse
                            + leftFalse * rightTrue
                            + leftTrue * rightTrue
                        )

                    else:
                        ans += leftFalse * rightFalse

                elif s[k] == "^":
                    if is_true:
                        ans += leftTrue * rightFalse + leftFalse * rightTrue

                    else:
                        ans += leftTrue * rightTrue + leftFalse * rightFalse

            return ans

        return helper(
            0, n - 1, True
        )  # calculating total ways for the solution for true expression


# Time Complexity: O(n × 2^n) => n for loop and 2^n for checking all the posssibilities
# Space Complexity: O(n) => for recursion


sol = SolutionRecur()
ans = sol.countWays("T^F|F")
print("ans_recur=", ans)  # 2 ways: ((T^F)|F) and (T^(F|F)).


# Memoized solution - here changing variables are i, j and is_true but is_true has two state only True/False
# so memo array will be memo[n+1][n+1][2]


# User function Template for python3
class SolutionMemo:
    def countWays(self, s):
        # code here
        # recursive solution
        n = len(s)

        # Memoized solution - here changing variables are i, j and is_true but is_true has two state only True/False
        # so memo array will be memo[n+1][n+1][2]

        memo = [[[-1] * 2 for _ in range(n + 1)] for _ in range(n + 1)]
        """
        n=4
        
        memo =
            
            [
              [ [-1,-1], [-1,-1], [-1,-1], [-1,-1], [-1,-1] ],
              [ [-1,-1], [-1,-1], [-1,-1], [-1,-1], [-1,-1] ],
              [ [-1,-1], [-1,-1], [-1,-1], [-1,-1], [-1,-1] ],
              [ [-1,-1], [-1,-1], [-1,-1], [-1,-1], [-1,-1] ],
              [ [-1,-1], [-1,-1], [-1,-1], [-1,-1], [-1,-1] ]
            ]

        
        """

        def helper(i, j, is_true):
            if i > j:  # crossed the j so no possible ways
                return 0

            if memo[i][j][is_true] != -1:
                return memo[i][j][is_true]

            if i == j:
                if is_true:
                    memo[i][j][1] = 1 if s[i] == "T" else 0
                    return memo[i][j][1]
                else:
                    memo[i][j][0] = 1 if s[i] == "F" else 0
                    return memo[i][j][0]

            ans = 0

            for k in range(i + 1, j, 2):

                # here we will calculate the true and false ways from left and right both side because the final ans depends on both side example if left is false and right is true then or of left, right comes true same vice versa

                leftTrue = helper(
                    i, k - 1, True
                )  # count total ways to get true for a given left expression, why k-1? because we want to get T/F string not operator
                leftFalse = helper(i, k - 1, False)
                rightTrue = helper(
                    k + 1, j, True
                )  # here again k+1 will be an operand means T/F string
                rightFalse = helper(k + 1, j, False)

                # check for the current operator |, &, ^, current index will be k

                if s[k] == "&":
                    if is_true:
                        # calculating for true
                        ans += (
                            leftTrue * rightTrue
                        )  # means if there are x ways to get true from left and y ways from right side then total ways will x*y because & checks for both true ways
                    else:
                        # calculating for False counts

                        ans += (
                            leftTrue * rightFalse
                            + leftFalse * rightTrue
                            + leftFalse * rightFalse
                        )

                elif s[k] == "|":
                    if is_true:
                        ans += (
                            leftTrue * rightFalse
                            + leftFalse * rightTrue
                            + leftTrue * rightTrue
                        )

                    else:
                        ans += leftFalse * rightFalse

                elif s[k] == "^":
                    if is_true:
                        ans += leftTrue * rightFalse + leftFalse * rightTrue

                    else:
                        ans += leftTrue * rightTrue + leftFalse * rightFalse

            memo[i][j][is_true] = ans

            return ans

        return helper(
            0, n - 1, True
        )  # calculating total ways for the solution for true expression


sol = SolutionMemo()
ans = sol.countWays("T^F|F")
print("ans_memo=", ans)  # 2 ways: ((T^F)|F) and (T^(F|F)).


# TC=> O(n x n x n) # n x n for state calculation for i and j and extra n for loop k
# SC=> O(n x n) + O(n) , first one for memo array and second for recursion stack
