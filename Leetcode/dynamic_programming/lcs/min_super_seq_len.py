class Solution:
    def minSuperSeq(self, str1, str2):
        #lets first analyse the str1 and st2 , you will find the longest common subseq

        # just minus it from the worst possible superseq which s1+s2

        n=len(str1)
        m=len(str2)

        memo=[[-1]*(m+1) for _ in range(n+1)]

        def helper(i, j):
            if i == 0 or j==0:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]


            if str1[i-1]==str2[j-1]:
                memo[i][j] = 1+helper(i-1,j-1)
            else:
                #return the max from both part
                memo[i][j]=max(helper(i-1,j), helper(i, j-1))

            return memo[i][j]



        lcs_len=helper(n,m)
        
        ans=n+m-lcs_len

        return ans
    
# TC=> O(n×m)
# SC=> O(n×m) + O(n+m)

sol_memo=Solution()
s1="AGGTAB"
s2="GXTXAYB"
ans_memo=sol_memo.minSuperSeq(s1,s2) 
print("ans_memo=",ans_memo) #9



class SolutionTab:
    def minSuperSeq(self, str1, str2):
        #lets first analyse the str1 and st2 , you will find the longest common subseq

        # just minus it from the worst possible superseq which s1+s2

        n=len(str1)
        m=len(str2)

        dp=[[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
        
        ans=n+m-dp[n][m]

        return ans
    

sol_tab=SolutionTab()
s1="AGGTAB"
s2="GXTXAYB"
ans_tab=sol_tab.minSuperSeq(s1,s2)
print("ans_tabulation=",ans_tab) #9
