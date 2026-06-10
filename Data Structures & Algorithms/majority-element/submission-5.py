class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}
        highest = 0
        res = None
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
            if hmap[num] > highest:
                highest = hmap[num]
                res = num
        
        return res