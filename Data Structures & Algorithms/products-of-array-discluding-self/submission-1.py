class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix_arr = [1] * n
        suffix_arr = [1] * n
        
        res = []
        for i in range(1, n):
            prefix_arr[i] = nums[i-1] * prefix_arr[i-1]
        
        for i in range(n-2, -1, -1):
            suffix_arr[i] = nums[i+1] * suffix_arr[i+1]
        
        for i in range(n):
            res.append(prefix_arr[i] * suffix_arr[i])
        return res
