class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1

        return sorted(hmap, key=hmap.get)[-k:]        