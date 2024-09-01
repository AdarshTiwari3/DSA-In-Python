class Solution:
    def checkValidString(self, s: str) -> bool:
        #count from both sides
        open=0
        for i in range(len(s)):
            if s[i]=='*' or  s[i]=='(':
                open+=1
            else:
                open-=1
                if open<0:
                    return 0 # means right already crossed the left parenthesis
        
        # check if open==0 means we have a valid string
        if open==0:
            return 1

        # check from back
        open=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='*' or s[i]==')': # match the closed
                open+=1
            else:
                open-=1
                if open<0:
                    return 0
        return 1
        
        
sol=Solution()
print(sol.checkValidString("()")) #1
print(sol.checkValidString("(*)")) #1
print(sol.checkValidString("(*))")) #1
print(sol.checkValidString("(*)))")) #0