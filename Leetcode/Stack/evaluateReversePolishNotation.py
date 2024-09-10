class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            # Check if the token is a number (either positive or negative)
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
               
                op1 = stack.pop()
                op2 = stack.pop()
                
                # Apply the operation
                if token == '+':
                    stack.append(op2 + op1)
                elif token == '-':
                    stack.append(op2 - op1)
                elif token == '*':
                    stack.append(op2 * op1)
                elif token == '/':
                    stack.append(int(op2 / op1))
        
        
        return stack[-1]
