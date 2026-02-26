import math
class SolutionMemo:
    def minCost(self, height):
        # code here
        n=len(height)
        memo=[-1] * (n+1)
        def helper(i):
            if i == n - 1:
                return 0
                
            if memo[i] != -1:
                return memo[i]
                
            one = abs(height[i+1]-height[i]) + helper(i+1)
            two=math.inf
            if i + 2 < n:
                two = abs(height[i+2]-height[i]) + helper(i+2)
            
            memo[i]= min(one, two)
            return memo[i]
            
            
            
        return helper(0)
    



class SolutionDP:
    def minCost(self, height):
        # code here
        n=len(height)
        dp=[0] * (n+1)
        
        
        for i in range(1, n):
            one=abs(height[i] - height[i-1]) + dp[i-1]
            
            two=math.inf
            
            if i>1:
                two=abs(height[i] - height[i-2]) + dp[i-2]
            
            dp[i]=min(one, two)
            
        return dp[n-1]
        
        

class SolutionDPOptimize:
    def minCost(self, height):

        prev2 = 0
        prev1 = 0

        for i in range(1, len(height)):

            one = abs(height[i] - height[i-1]) + prev1

            two = math.inf
            
            if i >= 2:
                two = abs(height[i] - height[i-2]) + prev2

            curr = min(one, two)

            prev2 = prev1
            prev1 = curr

        return prev1