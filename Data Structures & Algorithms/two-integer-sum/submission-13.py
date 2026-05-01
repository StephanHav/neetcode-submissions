class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num

            if hashmap.get(complement, None) != None:
                return [hashmap[complement], i]

            hashmap[num] = hashmap.get(num, i)