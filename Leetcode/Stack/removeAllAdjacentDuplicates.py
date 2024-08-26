class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        stack.append(s[0])
        for i in range(1,len(s)):
            j=0
            if stack and stack[-1]==s[i]:
                j=stack.pop()

            
            if not j:
                stack.append(s[i])
        
        return "".join(stack)

sol=Solution()
print(sol.removeDuplicates("abbaca")) #ca