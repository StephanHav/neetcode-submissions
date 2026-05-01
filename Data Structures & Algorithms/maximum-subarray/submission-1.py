class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        l = 0
        r = 0
        res = float("-inf") 
        while r < len(nums):
            if sum(nums[l:r+1]) >= nums[r]:
                res = max(res, sum(nums[l:r+1]))
                r += 1 
            else:
                res = max(res, nums[r])
                l = r
                r += 1

        return res