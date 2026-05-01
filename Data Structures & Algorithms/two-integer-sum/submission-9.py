class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for key in hashmap:
            complement = target - key
            if (hashmap.get(complement, 0) > 0 and complement != key):
                return [nums.index(key), nums.index(complement)]

            if (hashmap.get(complement, 0) > 1 and complement == key):
                return [nums.index(key), nums.index(key, nums.index(key)+1)]