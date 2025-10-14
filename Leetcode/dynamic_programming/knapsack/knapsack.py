#0/1 knapsack implementation using recursion

def knapsack(wt,val,w,n):
    if n==0 or w==0:
        return 0
    
    if wt[n-1]<=w:
        #return max from take or not take
        return max(val[n-1]+knapsack(wt,val,w-wt[n-1],n-1),knapsack(wt,val,w,n-1))
    elif wt[n-1]>w:
        return knapsack(wt,val,w,n-1)
    
wt=[1,3,4,5]
val=[1,4,5,7]
w=7

print(knapsack(wt,val,w,len(wt)))