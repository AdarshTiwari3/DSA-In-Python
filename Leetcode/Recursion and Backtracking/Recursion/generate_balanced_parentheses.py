from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans=[]

        def helper(curr,opened,closed):
            if opened==closed==0:
                ans.append(''.join(curr))
                return

            if opened>0:
                #move left otherwise parentheses will be invalid
                curr.append('(')
                helper(curr,opened-1,closed)
                curr.pop()
                

            if opened<closed:
                #move right else move left parentheses selection
                curr.append(')')
                helper(curr,opened,closed-1)
                curr.pop()
            

            
                
            
            
            
            
        helper([],n,n)
        return ans
sol=Solution()
print(sol.generateParenthesis(3))