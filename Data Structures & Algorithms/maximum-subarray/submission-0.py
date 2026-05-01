class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        res = float("-inf") 
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                # print(nums[i:j+1], sum(nums[i:j+1]))
                res = max(sum(nums[i:j+1]), res)
        return res