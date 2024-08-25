class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=''
        cnt=0
        for i in range(len(s)):
            if s[i]=='(':
                if cnt>0:
                    ans+='('
                cnt+=1
            else:
                cnt-=1
                if cnt>0:
                    ans+=')'
                    
        return ans

sol=Solution()
print(sol.removeOuterParentheses("(()())(())")) #()()()