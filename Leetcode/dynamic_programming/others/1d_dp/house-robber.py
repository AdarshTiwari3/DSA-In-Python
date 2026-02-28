from typing import List

class SolutionRecur:
    def rob(self, nums: List[int]) -> int:
        
        n =len(nums)

        def helper(ind) -> int:
            if ind >= n:
                return 0

            take=nums[ind]+helper(ind+2)
            not_take=helper(ind+1)
            return max(take, not_take)




        return helper(0)
    
# TC=> O(2^n)
# SC=> O(n) # recursion stack


class SolutionMemo:
    def rob(self, nums: List[int]) -> int:
        
        n =len(nums)
        # here changing variable is ind so ind can go from 0-n so memo array will be of n+1
        memo=[-1] * (n+1)
        def helper(ind) -> int:
            if ind >= n:
                return 0
            
            if memo[ind] != -1:
                return memo[ind]

            take=nums[ind]+helper(ind+2)
            not_take=helper(ind+1)
            memo[ind]= max(take, not_take)
            return memo[ind]




        return helper(0)
    

# TC=> O(n)
# SC=> O(n) + O(n) # recursion + memo array



class SolutionDP:
    def rob(self, nums: List[int]) -> int:
        
        n =len(nums)
        # here changing variable is ind so ind can go from 0-n so memo array will be of n+1
        dp=[0] * (n+1)
        dp[0]=0
        dp[1]=nums[0]
        
        for i in range(2, n+1): # should atleast start from 2 other wise dp[-1] which is not possible
            take=nums[i-1]+dp[i-2]
            not_take=dp[i-1]
            dp[i]=max(take, not_take)

        return dp[n]
    
# TC=> O(n)
# SC=> O(n) only dp array , we removed the recursion space


class SolutionMostOpti:
    def rob(self, nums: List[int]) -> int:
        
        n =len(nums)
        # here changing variable is ind so ind can go from 0-n so memo array will be of n+1
        
        prev2=0
        prev1=nums[0]
        
        for i in range(2, n+1): # should atleast start from 2 other wise dp[-1] which is not possible
            curr=max(nums[i-1]+prev2, prev1)
            prev2=prev1
            prev1=curr
            

        return prev1
    
# TC=> O(n)
# SC=> O(1) 
