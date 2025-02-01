from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def helper(ind,localArray):
            if len(localArray)==k:
                ans.append(list(localArray))
                return
            
            for i in range(ind,n+1):
                localArray.append(i)
                helper(i+1,localArray)
                localArray.pop()

        

        ans=[]
        helper(1,[])
        return ans
        
sol=Solution()
print(sol.combine(4,2)) # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]