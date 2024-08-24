from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr=operations
        stack=[]
        sum=0
        for i in range(len(arr)):
            
            if stack and arr[i]=='C':
                stack.pop()
            elif stack and arr[i]=='D':
                stack.append(stack[-1]*2)
            elif stack and arr[i]=='+':
                #  print("after-D",stack[-1],"stack=",stack)                
                 firstPoped=stack.pop()
                 newValue=firstPoped+stack[-1]
                 stack.append(firstPoped)                     
                 stack.append(newValue)
                 
                  
            else:
                stack.append(int(arr[i]))
        # print(stack)
        while len(stack):
            sum+=stack[-1]
            stack.pop()
            

        return sum
        
check=Solution()
print(check.calPoints(["5","2","C","D","+"])) #30