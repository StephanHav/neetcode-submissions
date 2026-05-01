class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [ 0 for i in cost ]
        dp[0] = cost[0]
        dp[1] = cost[1]

        ptr = 2
        while ptr != len(cost):
            dp[ptr] = min(cost[ptr]+dp[ptr-2], cost[ptr]+dp[ptr-1])
            ptr += 1
        
        return min(dp[-2], dp[-1])