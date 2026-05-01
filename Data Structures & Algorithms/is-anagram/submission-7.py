class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        balance = {}
        for char_s, char_t in zip(s, t):
            balance[char_s] = balance.get(char_s, 0) + 1
            balance[char_t] = balance.get(char_t, 0) - 1
        
        zeroes = True
        for key in balance:
            if balance[key] != 0:
                zeroes = False

        return zeroes
        