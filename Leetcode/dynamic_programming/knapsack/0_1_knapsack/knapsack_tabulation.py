
wt=[1,3,4,5]
val=[1,4,5,7]
n=len(val)
w=7

dp=[[0 for _ in range(w+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(w+1):
        # not required as base condition is already fulfilled
        # if i==0 or j==0:
        #     dp[i][j]=0
        #     continue
        take=0
        if wt[i-1]<=j:
            take=val[i-1]+dp[i-1][j-wt[i-1]]

        not_take=dp[i-1][j]
        dp[i][j]=max(take,not_take)

print("ans=",dp[n][w])
