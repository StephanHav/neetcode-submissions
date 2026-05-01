class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxvol = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if heights[i] >= heights[j]:
                    vol = heights[j] * (j - i)
                    if vol > maxvol:
                        maxvol = vol
                else:
                    vol = heights[i] * (j - i)
                    if vol > maxvol:
                        maxvol = vol
        return maxvol