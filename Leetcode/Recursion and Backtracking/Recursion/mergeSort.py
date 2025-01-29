class Solution:
    def mergeTwoSortedArray(self,arr1,arr2):
        arr=[]
        p1,p2=0,0
        # print("left=",arr1,"right=",arr2)
        while p1<=len(arr1)-1 and p2<=len(arr2)-1:
            if arr1[p1]<=arr2[p2]:
                arr.append(arr1[p1])
                p1+=1
            else:
                arr.append(arr2[p2])
                p2+=1
        arr.extend(arr1[p1:])
        arr.extend(arr2[p2:])
        return arr
            
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def helper(low,high,arr):
            if low==high:
                return [arr[low]]
            mid=(low+high)//2
            # print("mid=",mid)
            leftSortedArray=helper(low,mid,arr)
            rightSortedArray=helper(mid+1,high,arr)
            # print("leftSortedArray=",leftSortedArray)
            # print("rightSortedArray=",rightSortedArray)
            return self.mergeTwoSortedArray(leftSortedArray,rightSortedArray)


        return helper(0,len(nums)-1,nums)