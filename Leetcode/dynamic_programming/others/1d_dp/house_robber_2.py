from typing import List



class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        
        if n==1:
            return nums[0]

        
        def helper(ind, last):
            if ind > last:
                return 0


            take = nums[ind] + helper(ind + 2, last)
            not_take = helper(ind + 1, last)

            return max(take, not_take)



        #case 1 if we exclude the first element and case 2 if we exclude the last element

        return max(helper(1, n-1), helper(0, n-2))
    
# TC=> O(2^n)
# SC=> O(n)


class SolutionMemo:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        
        if n==1:
            return nums[0]

        # here changing variables are ind and last , ind so memo will be n+1 of size and last

        memo={}
        def helper(ind, last):
            if ind > last:
                return 0

            
            if (ind, last) in memo:
                return memo[(ind, last)]

            take = nums[ind] + helper(ind + 2, last)
            not_take = helper(ind + 1, last)

            memo[(ind, last)]=max(take, not_take)
            return memo[(ind, last)]



        #case 1 if we exclude the first element and case 2 if we exclude the last element

        return max(helper(1, n-1), helper(0, n-2))
    
# TC=> O(n)
# SC=> O(n x 2) + O(n) # recursion + memo map so total SC we can say will be O(n)
