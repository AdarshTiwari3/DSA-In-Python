from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j=0
        stack=[]
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1

        return not len(stack)


sol=Solution()

print(sol.validateStackSequences([1,2,3,4,5],[4,5,3,2,1])) #True