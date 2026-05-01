class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        len_nums = len(nums)
        dp = [1] * (len_nums)
        res = 1

        for i in range(len_nums-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    res = max(res, dp[i])
        return res
# [4,4,3,3,2,2,1]
# [9,1,i4,j2,3,3,7]
            
