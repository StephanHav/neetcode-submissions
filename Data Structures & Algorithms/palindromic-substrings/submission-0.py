class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        l = 0
        r = 0
        for i in range(len(s)):
            res += 1 #single char palindrome
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s): #Check bounds
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break
        return res