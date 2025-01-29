class Solution:
    def findPartitionIndex(self,arr,low,high):
        mid=(low+high)//2
        #sort the low,mid and high
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
        pivot=arr[mid]
        arr[low], arr[mid] = arr[mid], arr[low] #move pivot to first index
        i,j=low+1,high
        while i<=j:
            while i<=high and arr[i]<=pivot: #move to element which is greater than pivot
                i+=1

            while arr[j]>pivot and j>=low+1: # move to smaller than pivot
                j-=1
            
            #now swap then i and j
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        #swap pivot with j element as pivot has find its correct place
        arr[j],arr[low]=arr[low],arr[j]
        return j
    def quickSort(self,arr,low,high):
        if low<high:
            partitionIndex=self.findPartitionIndex(arr,low,high)
            self.quickSort(arr,low,partitionIndex-1)
            self.quickSort(arr,partitionIndex+1,high)
        
    def sortArray(self, nums: List[int]) -> List[int]:
        #Intuition- Quick Sort
        #1. pick a pivot and place it at correct position
        #2. left of the pivot should be less than pivot and right should be bigger than pivot
        #3. Repeat the steps
        #4 pivot can be any element , 1st mid last any
        self.quickSort(nums,0,len(nums)-1)
        return nums