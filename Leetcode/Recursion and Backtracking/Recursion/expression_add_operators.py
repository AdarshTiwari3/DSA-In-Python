class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        
        def helper(ind, currString, prevNum, currValue):
            if ind == len(num):
                if currValue == target:
                    ans.append(''.join(currString))
                return
            
            for i in range(ind, len(num)):
                if i>ind and num[ind] == '0':
                    break
                currNumString = num[ind:i+1]    
                currentNum = int(currNumString)
                
                if ind == 0:
                    helper(i+1, [currNumString], currentNum, currentNum)
                else:
                    #for +
                    helper(i+1, currString + ['+', currNumString], currentNum, currValue + currentNum)
                    # for -
                    helper(i+1, currString + ['-', currNumString], -currentNum, currValue - currentNum)
                    #for *
                    helper(i+1, currString + ['*', currNumString], currentNum * prevNum, currValue - prevNum + (prevNum * currentNum))

        helper(0, [], 0, 0)
        return ans
