class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()

        for c in range(len(s)):
            if s[c] == s[-c-1]:
                if c == int(len(s)/2):
                    return True
                continue
            else:
                return False
        return True