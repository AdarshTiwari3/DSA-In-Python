class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def helper(arr,ind,k):
            if len(arr)==1:
                return arr[0]

            ind=(ind+k)%len(arr) #coz of circular game
            arr.pop(ind)
            return helper(arr,ind,k)
            



        
        arr=[i+1 for i in range(n)]
        # print(arr)
        return helper(arr,0,k-1)
        