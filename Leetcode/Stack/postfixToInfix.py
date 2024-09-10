def postToInfix(postfix: str) -> str:
    # Write your code here.
    stack=[]
    for i in range(len(postfix)):
        if postfix[i].isalnum():
            stack.append(postfix[i])
        else:
            op1=stack.pop()
            op2=stack.pop()

            res="("+op2+postfix[i]+op1+")"

            stack.append(res)
        
    return stack[-1]

print(postToInfix("ABC/-AK/L-*")) # ((A-(B/C))*((A/K)-L))