class Solution:
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
    
# or 
class Solution:
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
        
    
class Solution:
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
        
        
        
             
        
        
        


