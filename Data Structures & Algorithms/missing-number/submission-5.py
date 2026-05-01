class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        
        check = 0
        sort = sorted(nums)
        for i, num in enumerate(sort):
            if check != num:
                return check
            check += 1
        return check
