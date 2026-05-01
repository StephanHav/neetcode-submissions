class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        balance = {}
        for char_s in s:
            if char_s in balance:
                balance[char_s] += 1
            else:
                balance[char_s] = 1
        
        for char_t in t:
            if char_t in balance:
                balance[char_t] -= 1
            else:
                balance[char_t] = -1
        
        zeroes = True
        for key in balance:
            if balance[key] != 0:
                zeroes = False

        return zeroes
        