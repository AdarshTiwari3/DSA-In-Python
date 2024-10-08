from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=deque()
        stack2=deque()
        for i in range(len(s)):
            if stack1 and s[i]=='#':
                stack1.pop()
            elif s[i]!='#':
                stack1.append(s[i])
            
        for i in range(len(t)):
            if stack2 and t[i]=='#':
                stack2.pop()
            elif t[i]!='#':
                stack2.append(t[i])
        
        return stack1==stack2

sol = Solution()
print(sol.backspaceCompare("ab#c","ad#c")) #True
            
            