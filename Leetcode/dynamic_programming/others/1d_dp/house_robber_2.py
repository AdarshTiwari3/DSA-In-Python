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



class SolutionDP:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        
        if n==1:
            return nums[0]

        def helper(start, last):
            new_len=last-start+1

            dp=[0] * (new_len+1)
            dp[0]=0
            dp[1]=nums[start]

            for i in range(2, new_len+1):
                dp[i]=max(nums[start + i-1]+dp[i-2], dp[i-1])

            return dp[new_len]


        #case 1 if we exclude the first element and case 2 if we exclude the last element

        case1=helper(1, n-1)
        case2=helper(0, n-2)
        return max(case1, case2)
    
# TC=> O(n)
# SC=> O(n) for dp array



class SolutionMostOptimize:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        
        if n==1:
            return nums[0]

        def helper(start, last):
            new_len=last-start+1

            
            prev2=0
            prev1=nums[start]

            for i in range(2, new_len+1):
                curr=max(nums[start + i - 1]+ prev2, prev1)
                prev2=prev1
                prev1=curr

            return prev1


        #case 1 if we exclude the first element and case 2 if we exclude the last element

        case1=helper(1, n-1)
        case2=helper(0, n-2)
        return max(case1, case2)
    
# TC=> O(n)
# SC=> O(1) 

