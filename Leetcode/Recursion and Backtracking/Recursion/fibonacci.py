class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        
        prev1,prev2=1,0

        for i in range(2,n+1):
            currSum=prev1+prev2
            prev1,prev2=currSum,prev1
        return prev1