class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans=0 #score
        stack=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(ans)
                ans=0
            elif s[i]==')':
                # print("stack=",stack,"top=",stack[-1])
                ans+=stack[-1]+max(ans,1)
                # print("ans=",ans)
                stack.pop()
        return ans
        
sol=Solution()
print(sol.scoreOfParentheses("(()(()))")) #6

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack=[0]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(0)
            elif s[i]==')':
               #calculate the value
               val=max(2*stack[-1],1)
               stack.pop()
               #now update the top of the stack with val+top
               stack[-1]+=val
        return stack[-1]
        
sol=Solution()
print(sol.scoreOfParentheses("(()(()))")) #6

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == '(':
                    score += 1 << depth #2*depth
        
        return score
s=Solution()
print(s.scoreOfParentheses("((()))")) #4
# Space complexity: O(1)