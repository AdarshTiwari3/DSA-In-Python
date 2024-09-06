class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans=0
        stack=[]
        stack.append(-1)
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                
                stack.pop()
                
                if stack==[]:
                    stack.append(i)
                else:
                    ans=max(ans,i-stack[-1])
                

        return ans
    
# Time complexity: O(n)
# Space complexity: O(n)
sol=Solution()
print(sol.longestValidParentheses("(()")) # 2
print(sol.longestValidParentheses(")()())")) # 4
print(sol.longestValidParentheses("")) # 0