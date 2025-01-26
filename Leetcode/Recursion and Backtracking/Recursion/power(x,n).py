class Solution:
    def myPow(self, x: float, n: int) -> float:
        # n is negative then the result will be 1/x^n, so in the both cases i have to calculate the x^n
        # approach- divide in the recursion for in divide by 2 means if we have 2^10 means it would be 2^5*2^5 and if 2^5 then as 5 is odd then 2*2^2*2^2


        def helper(x,n):
            if n==0:
                return 1
            if x==0:
                return 0

            multi=helper(x,n//2)
            multi=multi*multi # means 2^4 will be 2^2*2^2
            if n%2==1: #odd then multiply with x as well
                multi=multi*x
            return multi

        multiply=helper(x,abs(n))
        if n<0:
            return 1/multiply
        return multiply


#SC: O(1) solution
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n=-n
            x=1/x
        ans=1
        while n>0:
            if n%2==1:
                ans=ans*x
            
            x=x*x
            # print("x=",x,"n=",n,"ans=",ans)
            n//=2 #make the half
        return ans