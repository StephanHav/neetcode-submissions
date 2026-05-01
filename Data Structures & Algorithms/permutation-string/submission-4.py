class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hmap = {i+ord('a'): 0 for i in range(26)}
        window = hmap.copy()

        for c in s1:
            hmap[ord(c)] += 1
        
        l = 0
        r = len(s1) - 1

        for c in s2[l:r+1]:
            window[ord(c)] += 1

        if window == hmap:
            return True

        while r < len(s2)-1:

            l += 1
            r += 1                        
            window[ord(s2[l-1])] -= 1
            window[ord(s2[r])] += 1

            if window == hmap:
                return True
        
        return False
