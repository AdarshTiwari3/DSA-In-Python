class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        if n%2==0:
            return self.isPowerOfTwo(n//2)
        return False


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>=1 and log2(n)%1==0 # using the log property