class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                hmap = {}
                for key in s[i:j+1]:
                    hmap[key] = hmap.get(key, 0) + 1
                if len(s[i:j+1]) - max(hmap.values()) <= k:
                    res = max(res, len(s[i:j+1]))
        
        return res