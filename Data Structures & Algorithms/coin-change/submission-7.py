class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        
        dp = [ -1 for _ in range(amount+1) ]
        dp[0] = 0

        for i in range(1, amount+1):
            for val in coins:
                if val > i:
                    continue
                elif val == i:
                    dp[i] = 1
                else:
                    if dp[i-val] == -1:
                        continue
                    else:
                        if dp[i] == -1:
                            dp[i] = dp[i-val] + 1
                        else:
                            dp[i] = min(dp[i], dp[i-val] + 1)
        return dp[amount]



