from typing import List
class Solution:
    def MAH(self,arr):
        n=len(arr)
        left=[]
        stack=[]
        for i in range(n):
            while stack and arr[i]<=arr[stack[-1]]:
                stack.pop()
            if stack==[]:
                left.append(-1)
            else:
                left.append(stack[-1])
            stack.append(i)
        
        right=[0]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and arr[i]<=arr[stack[-1]]:
                stack.pop()
            if stack==[]:
                right[i]=n
            else:
                right[i]=stack[-1]
            stack.append(i)
        mxArea=0
        for i in range(n):
            mxArea=max(mxArea,(right[i]-left[i]-1)*arr[i])
        return mxArea
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # left,right,area=self.MAH([3,1,3,2,2])
        # print("NSL=",left,"NSR=",right, "Area=",area)
        mxArea=0
        n=len(matrix)
        m=len(matrix[0])
        histogram=[]
        for i in range(m):
            histogram.append(int(matrix[0][i]))
        mxArea=max(mxArea,self.MAH(histogram))
        for i in range(1,n):
            for j in range(m):
                if matrix[i][j]=='1': # add to the histogram
                    histogram[j]+=int(matrix[i][j])
                else:
                    histogram[j]=0
            print("Histogram=",histogram)
            mxArea=max(mxArea,self.MAH(histogram))
        return mxArea
        