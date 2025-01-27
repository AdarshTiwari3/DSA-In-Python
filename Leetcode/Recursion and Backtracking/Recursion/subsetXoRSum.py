class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(cur_ind, currSum):
            if cur_ind == n: 
                return currSum

            take_xor = helper(cur_ind + 1, currSum ^ nums[cur_ind]) 
            not_take_xor = helper(cur_ind + 1, currSum) 

            return take_xor + not_take_xor

        return helper(0, 0) 