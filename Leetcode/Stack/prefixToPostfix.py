from typing import List

def preToPost(s: str) -> str:
    stack = []
    for i in range(len(s)-1,-1,-1):
        if s[i].isalnum():
            stack.append(s[i])
        else:
            op1=stack.pop()
            op2=stack.pop()

            stack.append(op1+op2+s[i])

    return stack[-1]

print(preToPost("*+AB-CD")) # AB+CD-*