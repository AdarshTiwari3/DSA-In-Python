class Solution:
    def minRemoveToMakeValid(self, st: str) -> str:
        countOpen=0
        s=list(st)
        for i in range(len(s)):
            if s[i]=='(':
                countOpen+=1
            elif s[i]==')':
                # handle the case which start ) parentheses
                if countOpen==0:
                    s[i]="$" # give any character mark as an extra char
                else:
                    countOpen-=1
        #now we have marked the excessive ) parenthese with $
        # now we will mark closing parentheses with $ , this time we will check from back
        for i in range(len(s)-1,-1,-1): # n-1 to 0 with reversed order
            if countOpen and s[i]=='(': # means we have extra ( left
                s[i]='$'
                countOpen-=1
        ans=''  
        for i in range(len(s)):
            if s[i] != '$':
                ans+=s[i]

        return ans

sol=Solution()
print(sol.minRemoveToMakeValid("lee(t(c)o)de)")) #lee(t(c)o)de
print(sol.minRemoveToMakeValid("a)b(c)d")) #ab(c)d