class Solution:
    def climbStairs(self, n: int) -> int:
        
        l, r = 0, 1
        for _ in range(n):
            temp = l
            l = r
            r = temp + r 

        return r
