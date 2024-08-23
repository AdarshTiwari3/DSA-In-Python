class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if s[0]==']' or s[0]==')' or s[0]=='}':
            return 0
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            else:
                # check in the stack for its validation
                if stack and stack[-1]=='(' and s[i]==')':
                    stack.pop()
                elif stack and stack[-1]=='{' and s[i]=='}':
                    stack.pop()
                elif stack and stack[-1]=='[' and s[i]==']':
                    stack.pop()
                else:
                    return 0
                

        if stack:
            return 0
        return 1

        