class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def helper(index,localAns,arr):
            
            if index==len(arr):
                ans.append(localAns[:]) # we have used[:] to create a local copy to avoid any further changes as it is mutable
                return 
            
            #intution will be take and not method, and while going to not take will remove the last element from take as we are gonna for not take
            localAns.append(arr[index])
            take=helper(index+1,localAns,arr)
            localAns.pop()
            notTake=helper(index+1,localAns,arr)
            


        
        helper(0,[],nums)
        return ans