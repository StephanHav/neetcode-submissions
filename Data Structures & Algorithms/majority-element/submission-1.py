class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        for key in hmap:
            if hmap[key] > (len(nums) / 2):
                return key
