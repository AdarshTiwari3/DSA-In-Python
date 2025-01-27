class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                count += pow(2, right - left, mod) # can form this number of subsequences means for [3,5,6] we can have 4 - [3],[5],[3,6],[3,5] all are <=target
                count=count%mod
                left += 1
            else:
                right -= 1
        
        return count
