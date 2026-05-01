class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def max_rob(start, end):

            rob1, rob2 = 0, 0

            for num in nums[start:end+1]:
                temp = max(rob2, rob1 + num)
                rob1 = rob2
                rob2 = temp

            return rob2
        return max(max_rob(0, len(nums) - 2), max_rob(1, len(nums) - 1))