class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def helper(index,localArray):
            if index == len(nums):
                ans.append(localArray[:])
                return
            ans.append(localArray[:])

            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                localArray.append(nums[i])
                helper(i+1,localArray)
                localArray.pop()
            


        helper(0,[])
        return ans