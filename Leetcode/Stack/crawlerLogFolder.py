from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        # stack.append(logs[0])
        for i in range(len(logs)):
            if stack and logs[i]=="../":
                stack.pop()
            elif logs[i]=="./":
                continue
            elif logs[i]!="../":
                stack.append(logs[i])
                 
        print("stack=",stack)
        return len(stack)
        
sol=Solution()
print(sol.minOperations(["d1/","d2/","../","d21/","./"])) #2