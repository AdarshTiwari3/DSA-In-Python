
class SolutionRec:
    def longCommSubstr(self, s1, s2):
        # code here
        
        # it is a variation of LCS 
        # order can't be skiped so whenever we have discontinuation make the length of LCS here 0
        
        n=len(s1)
        m=len(s2)
        
        def helper(n , m, count):
            if n == 0 or m==0:
                return count
                
            if s1[n-1] == s2[m-1]:
                count= helper(n-1,m-1, count+1)
                
            count=max(count, helper(n,m-1, 0), helper(n-1,m, 0))
                
            return count
            
        
        
        
        return helper(n , m , 0)

sol_rec=SolutionRec()
s1="ABCDGH"
s2="ACDGHR"
ans_rec=sol_rec.longCommSubstr(s1,s2)
print("ans_rec=",ans_rec) #4
    
# or 
class SolutionRec2:
    def longCommSubstr(self, s1, s2):
        # code here
        
        # it is a variation of LCS 
        # order can't be skiped so whenever we have discontinuation make the length of LCS here 0
        
        n=len(s1)
        m=len(s2)
        self.count=0
        def helper(n , m):
            if n == 0 or m==0:
                return 0
                
            if s1[n-1] == s2[m-1]:
                currLen=1+helper(n-1,m-1)
                self.count=max(self.count, currLen)
            
            else:
                helper(n-1,m)
                helper(n,m-1)
                currLen=0
                
            return currLen
                
                
                
            
            
        
        
        
        helper(n , m)
        return self.count

sol_rec2=SolutionRec2()
s1="ABCDGH"
s2="ACDGHR"
ans_rec2=sol_rec2.longCommSubstr(s1,s2)
print("ans_rec2=",ans_rec2) #4

# TC=> O(2^(n+m)) SC=> O(n+m)
    
class SolutionMemo:
    def longCommSubstr(self, s1, s2):
        # code here
        
        # it is a variation of LCS 
        # order can't be skiped so whenever we have discontinuation make the length of LCS here 0
        
        n=len(s1)
        m=len(s2)
        
        memo=[[-1 for _ in range(m+1)] for _ in range(n+1)]
        self.count=0
        def helper(n , m):
            if n == 0 or m==0:
                return 0
                
            if memo[n][m] !=-1:
                return memo[n][m]
                
            if s1[n-1] == s2[m-1]:
                memo[n][m]=1+helper(n-1,m-1)
                self.count=max(self.count, memo[n][m])
                
            else:
                memo[n][m]=0
                
            helper(n-1,m)
            helper(n,m-1)
            return memo[n][m]
                
            
        
        
        helper(n,m)
        return self.count
        
        
        
             
        
sol_memo=SolutionMemo()
s1="ABCDGH"
s2="ACDGHR"
ans_memo=sol_memo.longCommSubstr(s1,s2)
print("ans_memo=",ans_memo) #4

# TC=> O(n x m) SC=> O(n x m) + O(n + m) 

# Tabulation solution


class SolutionTab:
    def longCommSubstr(self, s1, s2):
        # code here
        
        # tabulation solution
        n=len(s1)
        m=len(s2)
        
        dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
        
        ans=0 # or ans = -math.inf
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=0
                ans=max(ans,dp[i][j])
        
        return ans
                    
    
sol_tab=SolutionTab()
s1="ABCDGH"
s2="ACDGHR"
ans_tab=sol_tab.longCommSubstr(s1,s2)
print("ans_tab=",ans_tab) #4

# Time: O(n × m)

# Space: O(n × m)
 
        


