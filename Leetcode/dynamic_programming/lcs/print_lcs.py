
class LCSTab:
    def printLcs(self, x: str, y: str, n: int, m: int) -> str:
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if x[i - 1] == y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        

        # backtrack and the check the matrix if matches then move to i-1, j-1 else see the max from i-1, j and i, j-1 and move accordingly and reverse at the last
        i , j = n, m
        lcs=[]
        while i>0 and j>0:
            if x[i - 1] == y[j - 1]:
                lcs.append(x[i - 1])
                i-=1
                j-=1
            elif dp[i - 1][j] >= dp[i][j-1]:
                i-=1
            else:
                j-=1
        
        return "".join(reversed(lcs))
    
sol_tab=LCSTab()
x="acbcf"
y="abcdaf"

ans=sol_tab.printLcs(x, y, len(x), len(y))

print("ans=",ans) #abcf

x="abaaa"
y="baabaca"
ans=sol_tab.printLcs(x, y, len(x), len(y))

print("ans=",ans) #abaa

# TC=> O(n×m)+O(n+m)  here Backtracking = O(n + m)
# SC=> O(n × m) + O(min(n,m)) here lcs list= O(min(n,m))
        
    


