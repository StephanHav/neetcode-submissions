class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hmap = {}
        for char_s, char_t in zip(s, t):
            hmap[char_s] = hmap.get(char_s, 0) + 1
            hmap[char_t] = hmap.get(char_t, 0) - 1

        zeroes = True
        for key in hmap:
            if hmap[key] != 0:
                zeroes = False

        return zeroes 
        