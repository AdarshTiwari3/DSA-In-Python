class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.ans=0

        def helper(ind,degrees,cnt):
            if ind==len(requests): # all request processed
                for i in range(n):
                    if degrees[i]!=0: # after processing we got any unbalanced building so return 
                        return
                self.ans=max(self.ans,cnt)
                return 

            #take
            
            fromm,too=requests[ind]
            degrees[fromm]-=1
            degrees[too]+=1

            
            helper(ind+1,degrees,cnt+1)

            #backtrack
            degrees[fromm]+=1
            degrees[too]-=1
            #not take
            helper(ind+1,degrees,cnt)





        degrees=[0]*n # for all buildings as incoming and toogoing should be same then only its valid transfer

        helper(0,degrees,0)

        return self.ans