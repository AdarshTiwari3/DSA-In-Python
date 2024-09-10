def priority(s):
    priorityList = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}
    return priorityList.get(s, -1)

def prefixToInfixConversion(s: str) -> str:
    # Write your code here.
    n=len(s)
    stack=[]
    for i in range(n-1,-1,-1):
        if s[i].isalnum():
            stack.append(s[i])
        else:

            # if we get any operator then pop two operands and add with operand
            op1=stack.pop()
            op2=stack.pop()
            # wrap in a parenthesis
            res="("+op1+s[i]+op2+")"

            #push into the stack again
            stack.append(res)

    return stack[-1]

print(prefixToInfixConversion("*+AB-CD")) # ((A+B)*(C-D))