class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None

        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
