def priority(s):
    priorityList = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}
    return priorityList.get(s, -1)

def infixToPrefix(exp: str) -> str:
    # Start from the right side of the expression
    i = len(exp) - 1
    stack = []
    ans = ""
    
    while i >= 0:
        if exp[i].isalnum():  # If operand, add to the result
            ans = exp[i] + ans
        elif exp[i] == ')':  # If closing parenthesis, push to the stack
            stack.append(')')
        elif exp[i] == '(':  # If opening parenthesis, pop till closing one
            while stack and stack[-1] != ')':
                ans = stack.pop() + ans
            stack.pop()  # Discard the ')'
        else:
            # While the precedence of the current operator is less than or equal to
            # the precedence of the operator on the stack, pop the stack
            while stack and priority(exp[i]) < priority(stack[-1]):
                ans = stack.pop() + ans
            stack.append(exp[i])  # Push the current operator to the stack
        i -= 1
    
    # Pop all remaining operators from the stack
    while stack:
        ans = stack.pop() + ans
    
    return ans

# Test the function
print(infixToPrefix("(a+b)+(c*d)-e*f"))  # Expected output: "-+ab+*cd*ef"
