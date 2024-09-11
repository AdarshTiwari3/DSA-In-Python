def postfixToPrefix(s: str) -> str:
    # Write your code here.
    stack=[]
    for i in range(len(s)):
        if s[i].isalnum():
            stack.append(s[i])
        else:
            op1=stack.pop()
            op2=stack.pop()
            stack.append(s[i]+op2+op1)

    return stack[-1]

print(postfixToPrefix("ABC/-AK/L-*")) # *-A/BC-/AKL