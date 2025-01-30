class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        def helper(index):
                if index==len(nums):
                    ans.append(nums[:])
                    return

                for i in range(index,len(nums)):
                    #swap from index to len(nums)-1
                    #swap the i with index
                    nums[index],nums[i]=nums[i],nums[index]
                    helper(index+1)
                    #backtrack as we have swapped so put it in previous position
                    nums[index],nums[i]=nums[i],nums[index]

        
        helper(0)
        return ans