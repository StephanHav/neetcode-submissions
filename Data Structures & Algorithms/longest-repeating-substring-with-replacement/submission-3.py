class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        l = 0
        r = 0
        hmap = {}
        hmap[s[r]] = 1
        while r < len(s):

            if len(s[l:r+1]) - max(hmap.values()) <= k:
                res = max(res, len(s[l:r+1]))
                r += 1
                if r < len(s):
                    hmap[s[r]] = hmap.get(s[r], 0) + 1 

            else:
                hmap[s[l]] = hmap.get(s[l], 0) - 1 
                l += 1
        return res

       #  A A A B A B B 
       #  0 1 2 3 4 5 6