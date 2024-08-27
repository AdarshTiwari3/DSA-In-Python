from collections import deque
class Solution:
    def makeGood(self, s: str) -> str:
        stack=deque()
        for i in range(len(s)):
            if stack and (stack[-1]==chr(ord(s[i])+32) or stack[-1]==chr(ord(s[i])-32)):
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)

sol=Solution()
print(sol.makeGood("leEeetcode")) #leetcode