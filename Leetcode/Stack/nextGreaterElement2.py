from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr=nums+nums
        i=len(arr)-1
        stack=[]
        ans=[]
        while i >=0:
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if i<=len(nums)-1:
                if stack==[]:
                    ans.append(-1)
                else:
                    ans.append(stack[-1])
            
            stack.append(arr[i])
            i-=1
        return ans[::-1]
    
sol=Solution()
print(sol.nextGreaterElements([1,2,1])) #[2,-1,2]