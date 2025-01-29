class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def helper(index,target,localArray):
            if index==len(candidates):
                if target==0:
                    ans.append(localArray[:])
                
                return

            # check for target if it is in range then only call the repeatitive element to be taken
            if candidates[index]<=target:
                localArray.append(candidates[index])
                helper(index,target-candidates[index],localArray) # take
                localArray.pop()
            
            helper(index+1,target,localArray) #not take


        helper(0,target,[])
        return ans