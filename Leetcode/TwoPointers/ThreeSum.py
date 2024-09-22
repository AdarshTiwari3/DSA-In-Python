from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            # print("i=",i,"j=",j)
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                while j<k:
                    # print("nums[j]+nums[k]=",nums[j]+nums[k],"nums[i]=",-nums[i])
                    if nums[j]+nums[k]==-nums[i]:
                        ans.append([nums[i],nums[j],nums[k]])
                        j+=1
                        k-=1
                        while nums[j] == nums[j-1] and j < k:
                            j += 1
                        
                    elif nums[j]+nums[k]<-nums[i]:
                        j+=1
                    else:
                        k-=1
        return ans
    

sol=Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4])) #[[-1,-1,2],[-1,0,1]]