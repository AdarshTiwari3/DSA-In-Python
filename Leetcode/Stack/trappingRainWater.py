from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # 1- find left maximum and right maximum now water can be stored in b/w two but min can only hold the water
        # 2- min(maxLeft,maxRight)
        # 3- water[i]=min(maxLeft-maxRight)-height[i]

        n=len(height)
        maxLeft=[0]*(n)
        maxRight=[0]*(n)
        maxLeft[0]=height[0]
        print("left=",maxLeft,"right=",maxRight)
        for i in range(1,n):
            print("i=",i,"height=",height[i],"maxLeft[i-1]=",maxLeft[i-1])
            maxLeft[i]=max(maxLeft[i-1],height[i])
            print("maxLeft[i]=",maxLeft[i])
        
        maxRight[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            maxRight[i]=max(height[i],maxRight[i+1])

        # calculate width in maxRight and ans
        ans=0
        for i in range(n):
            maxRight[i]=min(maxLeft[i],maxRight[i])
            ans+=maxRight[i]-height[i]

        return ans
            
