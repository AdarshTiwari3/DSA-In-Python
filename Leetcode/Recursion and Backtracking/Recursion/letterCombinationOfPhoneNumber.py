from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsChar={
            "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }
        #TC= O(n*4^n) as for 9 we can have maximum 4 combinations wxyz
        
        ans=[]

        def helper(index,currString):
            if len(currString)==len(digits):
                ans.append(''.join(currString))
                return

            correspondingChars=digitsChar[digits[index]]   #get from map/dictionary
            #loop for every character
            for char in correspondingChars:
                currString.append(char)
                helper(index+1,currString)
                currString.pop()
        if digits=="":
            return []
        helper(0,[])
        return ans
    
sol=Solution()
print(sol.letterCombinations("23")) # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]