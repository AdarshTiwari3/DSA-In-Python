class Solution:
    def allLCS(self, s1, s2):
        # Code here
        
        n, m = len(s1), len(s2)

        # Step 1: Build DP table (length only)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        
        # step -2 backtrack to all possibilities and store in memo
        memo=[[None]*(m+1) for _ in range(n+1)] # None because we are storing entire set object
        
        def backtrack(i, j):
            if i == 0 or j == 0:
                return {""}
                
            if memo[i][j] is not None:
                return memo[i][j] # it will contain the elements of set e.g {"ab","ac"}
                
            ans=set()
            
            if s1[i-1]==s2[j-1]:
                
                for seq in backtrack(i-1,j-1): #because it will be set of all possibilties string so loop here
                    ans.add(seq+s1[i-1])
                    
            else:
                if dp[i-1][j]>=dp[i][j-1]:
                    ans = ans | backtrack(i-1, j) # it is doing union of set mean getting all the unique possible values
                
                if dp[i][j-1] >= dp[i-1][j]:
                    ans = ans | backtrack(i, j-1)
            
            memo[i][j]=ans
            return ans
            
        
        return sorted(backtrack(n, m)) # this converts the set of strings into an array and also sort this into  lexicographical order.

    

s1="abaaa"
s2="baabaca"

sol=Solution()
ans=sol.allLCS(s1,s2)
print("ans=",ans)

# TC=> O(nxm) + O(K x L) ---> k = sequence and L is length of each seq
# or TC=> O(n x m+ K x L+ K logK x L)
# K = number of LCS
# L = length of each LCS


# SC=> O(nxm) + O(K x L)