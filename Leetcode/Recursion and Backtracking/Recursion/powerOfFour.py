class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        if n%4==0:
            return self.isPowerOfFour(n//4)
        return False
    

#optimized solution
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        logOfNumBase4=math.log(n)/math.log(4)
        # print("logBase4=",logOfNumBase4)
        return logOfNumBase4%1==0

