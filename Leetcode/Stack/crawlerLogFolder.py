from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt=0
        for i in range(len(logs)):
            if logs[i]=="../":
                cnt-=1
                if cnt<0:
                    cnt=0
            elif logs[i]=='./':
                continue
            elif logs[i]!='../':
                cnt+=1

        return cnt
        
        
sol=Solution()
print(sol.minOperations(["d1/","d2/","../","d21/","./"])) #2