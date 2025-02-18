from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = set()
        min_removed = float('inf')

        def is_valid(currString):
            balance = 0
            for char in currString:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        def helper(ind, currString, removed_count):
            nonlocal min_removed
            if ind == len(s):
                if is_valid(currString):
                    if removed_count < min_removed:
                        min_removed = removed_count
                        ans.clear()
                    if removed_count == min_removed:
                        ans.add(''.join(currString))
                return

            if s[ind] == '(' or s[ind] == ')':
                currString.append(s[ind])
                helper(ind + 1, currString, removed_count) 
                currString.pop()
                helper(ind + 1, currString, removed_count + 1) 
            else:
                helper(ind + 1, currString + [s[ind]], removed_count)

        helper(0, [], 0)
        return list(ans)
    
sol=Solution()
print(sol.removeInvalidParentheses("()())()"))