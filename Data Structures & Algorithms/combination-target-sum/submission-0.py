class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        current = 0
        
        def dfs(i, current_sum: int, current_combi: List[int]):
            if current_sum == target:
                res.append(current_combi.copy())
                return
            if i >= len(nums) or current_sum > target:
                return

            current_combi.append(nums[i])
            dfs(i, current_sum + nums[i], current_combi)
            current_combi.pop()
            dfs(i+1, current_sum, current_combi)


        dfs(0, 0, [])
        return res

 
# nums = [2,5,6,9] 
# target = 9

