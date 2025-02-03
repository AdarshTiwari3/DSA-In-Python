class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def helper(index,currPath,target):
            if len(currPath)==k:
                if target==0:
                    ans.append(list(currPath))
                return 

            for i in range(index,10):
                if target-i>=0:
                    currPath.append(i)
                    helper(i+1,currPath,target-i)
                    #backtrack
                    currPath.pop()


        
        ans=[]
        if n<k:
            return ans
        helper(1,[],n)
        return ans