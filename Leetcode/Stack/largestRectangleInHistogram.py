from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # lets find out next smaller to right and next smaller to left at any given index
        stack=[]
        i=len(heights)-1
        right=[]
        while i >=0:
            while stack and stack[-1][0]>=heights[i]:
                stack.pop()

            if stack==[]:
                right.append(len(heights))
            else:
                right.append(stack[-1][1])
            stack.append((heights[i],i))
                


            i-=1
        stack=[]
        left=[]
        for i in range(len(heights)):
            while stack and stack[-1][0]>=heights[i]:
                stack.pop()

            if stack==[]:
                left.append(-1)
            else:
                left.append(stack[-1][1])
            stack.append((heights[i],i))

        print("Left=",left)
        print("right",right[::-1])  
        n=len(left)
        width=[0]*n
        
        for i in range(len(left)):
            width[i]=right[n-1-i]-left[i]-1
        print("width=",width)
        ans=0
        for i in range(n):

            ans=max(ans,heights[i]*width[i])


            
        return ans
        

#more optimised solution
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)
        for i in range(n):
            print("stack=",stack)
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        while stack:
            height = heights[stack.pop()]
            if not stack:
                width = n
            else:
                width = n - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area
