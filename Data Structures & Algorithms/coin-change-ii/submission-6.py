from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        
        @cache
        def dfs(i, to_collect):
            if i == len(coins) or to_collect < 0:
                return 0
            
            if not to_collect: 
                return 1

            pick = dfs(i, to_collect - coins[i])
            
            skip = dfs(i+1, to_collect)
            return pick + skip
        
        return dfs(0, amount)
 