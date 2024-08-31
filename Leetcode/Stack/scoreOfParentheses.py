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