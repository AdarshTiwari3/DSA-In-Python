class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def helper(index, currString):
            if index == len(s):
                ans.append(''.join(currString))
                return
            
            if s[index].isalpha():
                currString.append(s[index].lower())
                helper(index + 1, currString)
                currString.pop()
                
                currString.append(s[index].upper())
                helper(index + 1, currString)
                currString.pop()
            else:
                currString.append(s[index])
                helper(index + 1, currString)
                currString.pop()

        ans = []
        helper(0, [])
        return ans
