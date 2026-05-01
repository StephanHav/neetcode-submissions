class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            elif nums[l] <= nums[mid]: #left is sorted
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                    if nums[r] == target:
                        return r
                else: 
                    l = mid + 1
                    if nums[l] == target:
                        return l

            else: #Right is sorted
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                    if nums[l] == target:
                        return l
                else:
                    r = mid - 1
                    if nums[r] == target:
                        return r

        if len(nums) == 1 and nums[0] == target:
            return 0

        return -1 

