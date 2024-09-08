def priority(s):
    if s in "+-*/^":
        priorityList={'+':0 ,'-':0, '*':1, '/':1, '^':2}

        return priorityList[s]
    return -1

def infixToPostfix(exp: str) -> str:
    # Write your code here.
    i=0
    n=len(exp)
    stack=[]
    ans=""
    # print(i,n,stack,ans)
    while i < n:
        if exp[i].isalnum():
            ans+=exp[i]
        elif exp[i]=='(':
            #push into the stack
            stack.append('(')
        elif exp[i]==')':
            # pop untill you get (
            while stack and stack[-1] != "(":
                ans+=stack.pop()
            
            # remove ( after this
            stack.pop()
        else:
            # you get any operand means ^ / * - +
            while stack and priority(exp[i]) <= priority(stack[-1]):
                ans+=stack.pop() # suppose exp[i]='-' and top='^'
            #put the current exp[i]
            stack.append(exp[i])
        i+=1
    # print("ans=",ans)
    # print("stack=",stack)
    while stack:
        ans+=stack.pop()


    return ans

print(infixToPostfix("a+b*(c^d-e)^(f+g*h)-i")) # abcd^e-fgh*+^*+i-