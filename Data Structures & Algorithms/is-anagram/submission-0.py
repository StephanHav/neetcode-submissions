class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s = {}
        map_t = {}
        for char_s, char_t in zip(s, t):
            if char_s in map_s:
                map_s[char_s] += 1
            else:
                map_s[char_s] = 1
            
            if char_t in map_t:
                map_t[char_t] += 1
            else:
                map_t[char_t] = 1
        
        if map_s == map_t:
            return True
        return False
        