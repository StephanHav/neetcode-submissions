class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)

        res = 0
        for unique in uniques:
            seq = 1
            if (unique - 1) not in uniques:
                while (unique + seq) in uniques:
                    seq += 1
                res = max(res, seq)
        return res