class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        to_jump = 0
        for i in range(len(nums)-2, -1, -1):
            print(nums[i])
            if nums[i] <= to_jump:
                to_jump += 1
            else:
                to_jump = 0
        return True if not to_jump else False