from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        

        def helper(index,currPart):
            if len(currPart)==4: # means found the valid ip address
                if index==len(s): #processed the entire given string now put the curr ip address into ans
                    ans.append('.'.join(currPart)) # means ["255","255","11","135"]
                    return

            for i in range(1,4): #to process only 1-3 digits limit which is given from 0 to 255
                if index+i<=len(s): #boundary check  so that it can't go beyond given string
                    local_part=s[index:index+i] # like 9:9+2 ="35"
                    #check if it lies in the range b/w 0-255 and not leading zero, if it is of 0 length then acceptable , not like 011
                    if len(local_part)==1 or (int(local_part)<=255 and local_part[0] != '0'):
                        currPart.append(local_part)
                        helper(index+i,currPart)
                        #backtrack
                        currPart.pop()

        ans=[]
        if 4<=len(s)<=12: # minimum should be of 4 length like 0.0.0.0 and maximum should be of 12 length like 255.255.255.255
            helper(0,[])
        return ans

sol=Solution()
print(sol.restoreIpAddresses("25525511135")) # ["255.255.111.35", "255.255.11.135"]