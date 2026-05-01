class Solution:
    def findMin(self, nums: List[int]) -> int:
        strLen = len(nums)
        l = 0
        r = strLen - 1
        while l < r:
            mid = (r + l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[r]