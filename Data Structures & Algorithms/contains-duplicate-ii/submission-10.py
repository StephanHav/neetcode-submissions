class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 1

        while l < r and r < len(nums):
            
            diff = abs(l - r)
            if nums[l] == nums[r] and diff <= k:
                return True
            print(l, r)
            if nums[l] != nums[r] and r < len(nums) - 1 and (diff < k or diff == 1):
                r += 1
                print('R + 1')
            else:
                print('L + 1')
                l += 1
        
        return False
        
# nums=[l0,1,2,3,r2,5]
# k=3