

def knapsack(wt,val,w,n):
    if n==0 or w==0:
        return 0
    
    if dp[n][w]!=-1:
        return dp[n][w]

    take=0

    if wt[n-1]<=w:
        take=val[n-1]+knapsack(wt,val,w-wt[n-1],n-1)

    not_take=knapsack(wt,val,w,n-1)

    dp[n][w]=max(take,not_take)

    return dp[n][w]



wt=[1,3,4,5]
val=[1,4,5,7]
n=len(val)
w=7
dp=[[-1 for _ in range(w+1)] for _ in range(n+1)]
print("ans=",knapsack(wt,val,w,n))