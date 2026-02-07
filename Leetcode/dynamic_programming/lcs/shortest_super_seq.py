class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Build the LCS table first.
        # Then use it to construct the shortest common supersequence.

        n=len(str1)
        m=len(str2)

        dp=[[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
        
        # step 2 - backtrack and build the super seq

        i , j , ans= n, m , []

        while i>0 and j>0:

            if str1[i-1] == str2[j-1]: # If characters match, include it once (part of LCS)
                ans.append(str1[i-1])
                i-=1
                j-=1
            else:
                if dp[i-1][j] >= dp[i][j-1]:
                    ans.append(str1[i-1]) # Move up: include character from str1 since it's not part of LCS here

                    i-=1
                else:
                    ans.append(str2[j-1]) # Move left: include character from str2
                    j-=1
        # append the remaining of elements of the string
        
        while i > 0:
            ans.append(str1[i-1])
            i-=1

        while j > 0:
            ans.append(str2[j-1])
            j-=1

       

        return "".join(reversed(ans))
    
sol=Solution()
str1 = "abac"
str2 = "cab"
ans=sol.shortestCommonSupersequence(str1,str2)
print("ans=",ans) #cabac