class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0 
        r = len(heights) - 1
        maxvol = 0
        while l < r:
            if heights[l] >= heights[r]:
                vol = heights[r] * (r - l)
                r -= 1
                if vol > maxvol:
                    maxvol = vol
            else:
                vol = heights[l] * (r - l)
                l += 1
                if vol > maxvol:
                    maxvol = vol

        # maxvol = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         if heights[i] >= heights[j]:
        #             vol = heights[j] * (j - i)
        #             if vol > maxvol:
        #                 maxvol = vol
        #         else:
        #             vol = heights[i] * (j - i)
        #             if vol > maxvol:
        #                 maxvol = vol
        return maxvol