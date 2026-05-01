class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1

        arr = [[] for i in range(len(nums) + 1)]
        for num, count in hmap.items():
            arr[count].append(num)

        output = []
        for i in range(len(arr)-1, 0, -1):
            for n in arr[i]:
                output.append(n)
                if len(output) == k:
                    return output