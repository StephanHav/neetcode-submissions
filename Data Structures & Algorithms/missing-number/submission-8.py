class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None

        res = len(nums)
        for i, num in enumerate(nums):
            res = res ^ i ^ num
        return res
