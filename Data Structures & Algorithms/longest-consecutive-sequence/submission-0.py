class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)

        res = 0
        for i in range(len(nums)):
            seq = 1
            if (nums[i] - 1) not in uniques:
                while (nums[i] + seq) in uniques:
                    seq += 1
                res = max(res, seq)
        return res