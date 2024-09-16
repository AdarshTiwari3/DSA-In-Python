class Solution:
    def squareOfNums(self,num):
        ans=0
        while num:
            lastDigit=num%10
            ans+=lastDigit*lastDigit
            num//=10
        return ans
    def isHappy(self, n: int) -> bool:
        # use slow and fast pointer

        slow=self.squareOfNums(n)
        fast=self.squareOfNums(slow)

        while slow!=fast:
            slow=self.squareOfNums(slow)
            fast=self.squareOfNums(self.squareOfNums(fast))
            if fast==True:
                return True

        return fast==True

sol=Solution()
print(sol.isHappy(19)) #True