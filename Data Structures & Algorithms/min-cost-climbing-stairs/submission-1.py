class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        first = cost[0]
        second = cost[1]

        ptr = 2
        while ptr != len(cost):
            temp = second
            second = min(cost[ptr]+first, cost[ptr]+second)
            first = temp
            ptr += 1
        
        return min(first, second)