class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in range(len(s)):
            if stack and stack[-1]=="(" and s[i]==')':
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)
    
sol=Solution()
print(sol.minAddToMakeValid("())")) #1


#optimized solution
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_unmatched = 0  # Tracks unmatched '('
        right_unmatched = 0  # Tracks unmatched ')'

        for char in s:
            if char == '(':
                left_unmatched += 1
            elif char == ')':
                if left_unmatched > 0:
                    left_unmatched -= 1  # Match a ')' with a '('
                else:
                    right_unmatched += 1  # Unmatched ')'
        
        return left_unmatched + right_unmatched
