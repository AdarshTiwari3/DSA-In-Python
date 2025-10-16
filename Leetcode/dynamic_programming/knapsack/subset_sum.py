
#recursion solution but it will through TLE

class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        def helper(ind,summ):
            if summ==0:
                return True
                
            if ind>=len(arr):
                return False
                
            take=0
            if arr[ind]<=summ:
                take=helper(ind+1,summ-arr[ind])
                
            not_take=helper(ind+1,summ)
            return take or not_take
            
        return helper(0,sum)
        

#memoization

class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        # (n+1)x(sum+1) dp array size
        dp=[[-1 for _ in range(sum+1)] for _ in range(len(arr)+1)]
        def helper(ind,summ):
            if summ==0:
                return True
                
            if ind>=len(arr):
                return False
                
            if dp[ind][summ]!=-1:
                return dp[ind][summ]
                
            take=False
            if arr[ind]<=summ:
                take=helper(ind+1,summ-arr[ind])
                
            not_take=helper(ind+1,summ)
            
            dp[ind][summ]=take or not_take
            
            return dp[ind][summ]
            
        return helper(0,sum)
    
sol=Solution()
arr=[3, 34, 4, 12, 5, 2]
summm=9
print("isSubsetSum=",sol.isSubsetSum(arr,summm))