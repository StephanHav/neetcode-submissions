class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        l = 0
        for r in range(len(s)):
            hmap = {}
            for key in s[l:r+1]:
                hmap[key] = hmap.get(key, 0) + 1
            if len(s[l:r+1]) - max(hmap.values()) <= k:
                res = max(res, len(s[l:r+1]))
            else: 
                l += 1
        return res

       #  A A A B A B B 
       #  0 1 2 3 4 5 6