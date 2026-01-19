from typing import List


class Solution:
    def unboundedKnapsack(self, W: int, wt: List[int], val: List[int]) -> int:
        n = len(wt)

        def helper(ind, capacity):
            """
            Generic base case (correct but slower):
            if capacity == 0 or ind < 0:
                return 0

            This version keeps recurring on index 0 and causes extra recursive calls.
            """

            if capacity == 0:
                return 0

            # optimized base case

            if ind == 0:
                # last element is left so why can't we get the max possible choices means if values at index is 2 and left capacity is 8 so we will go and pick 2 four times

                possible_times = capacity // wt[0]  # means example 8//2 =4

                return possible_times * val[0]

            pick = 0
            if wt[ind] <= capacity:
                pick = val[ind] + helper(ind, capacity - wt[ind])

            not_pick = helper(ind - 1, capacity)

            return max(pick, not_pick)

        return helper(n - 1, W)


sol = Solution()
# sol.unboundedKnapsack()
