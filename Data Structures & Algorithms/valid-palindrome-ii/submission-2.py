class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        whole = True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif self.isPalindrome(s, l+1, r):
                return True
            elif self.isPalindrome(s, l, r-1):
                return True
            else:
                return False
        return True

    def isPalindrome(self, s, l, r):

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True