#User function Template for python3
class Solution:
    def NBitBinary(self, n):
        # code here
        
        ans=[]
        def helper(curr,one,zero):
            if len(curr)==n:
                ans.append(''.join(curr))
                return
            
            #valid move always chose 1's , invalid when zero<one means more 0's have been selected than 1
            
            if one>0:
                curr.append('1')
                helper(curr,one-1,zero)
                curr.pop()
            if one<zero:
                curr.append('0')
                helper(curr,one,zero-1)
                curr.pop()
            
            
            
        helper([],n,n)
        return ans
    

runner=Solution()

print(runner.NBitBinary(3))