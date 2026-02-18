# Backtracking Solution
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # solve it using normal backtracking
        n = len(s)

        ans = []

        def isPalin(left, right) -> bool:
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False

            return True

        def helper(ind, curr):
            if ind == n:
                ans.append(curr[:])
                return

            for end in range(ind, n):
                if isPalin(ind, end):
                    curr.append(s[ind : end + 1])
                    helper(end + 1, curr)
                    curr.pop()

        helper(0, [])

        return ans


sol = Solution()
ans = sol.partition("aab")
print("ans=", ans)  # ans= [['a', 'a', 'b'], ['aa', 'b']]
