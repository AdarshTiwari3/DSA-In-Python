class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def helper(ind,currPath):
            if len(currPath)>=2:
                ans.append(list(currPath))
            
           
            seen=set() 

            for i in range(ind,len(nums)):
                if nums[i] in seen:
                    continue
                if not currPath or nums[i] >= currPath[-1]:
                    seen.add(nums[i])
                    currPath.append(nums[i])
                    helper(i+1,currPath)
                    currPath.pop() #backtrack
                    

        ans=[]
        helper(0,[])
        return ans
    

