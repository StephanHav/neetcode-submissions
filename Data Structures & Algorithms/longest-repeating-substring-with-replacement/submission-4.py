class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        l = 0
        r = 0
        hmap = {}
        hmap[s[r]] = 1
        while r < len(s):

            if (r - l + 1) - max(hmap.values()) <= k:
                res = max(res, r - l + 1)
                r += 1
                if r < len(s):
                    hmap[s[r]] = hmap.get(s[r], 0) + 1 

            else:
                hmap[s[l]] = hmap.get(s[l], 0) - 1 
                l += 1
        return res
