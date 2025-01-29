from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        
        def helper(index, target, localArray):
            if target == 0:
                ans.append(localArray[:])
                return
            if index == len(candidates):
                return
            # check all the possible picks at every index and don't repeat if picked up element is already same as current one
            for i in range(index,len(candidates)):
                if i > index and candidates[i]==candidates[i-1]: # no need to take that , simply skip duplicates
                    continue
                if candidates[i]>target:
                    break # no need to go further
                localArray.append(candidates[i])
                helper(i+ 1, target - candidates[i], localArray)
                localArray.pop()

            

        helper(0, target, [])
        return ans

sol=Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5],8)) # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]