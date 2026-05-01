class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        output = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:

                        output.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        
        return list(output)
                