class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def checkPalindromes(l, r):
            nonlocal res

            while l >= 0 and r < len(s): #Check bounds
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break
            return 
        
        for i in range(len(s)):
            checkPalindromes(i, i)
            checkPalindromes(i, i + 1)

        return res