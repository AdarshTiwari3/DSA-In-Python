from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def helper(index):
                if index==len(nums):
                    ans.append(nums[:])
                    return
                seen=set()
                for i in range(index,len(nums)):
                    
                    #swap index with i to get diff permutations from index to n-1               
                    if nums[i] in seen:
                        continue
                    seen.add(nums[i])
                    nums[index],nums[i]=nums[i],nums[index]
                    helper(index+1)
                    #backtrack
                    nums[index],nums[i]=nums[i],nums[index]


        ans=[]           
        helper(0)
        return ans
    
sol=Solution()
print(sol.permuteUnique([1,1,2])) # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]