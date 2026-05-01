import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1

        heap_list = []
        for key in hmap:
            tup = tuple([hmap[key] * -1, key])
            heap_list.append(tup)
        
        heapq.heapify(heap_list)
        
        output = []
        while k > 0:
            output.append(heapq.heappop(heap_list)[1])
            k -= 1

        return output