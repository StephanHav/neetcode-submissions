class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 1
        window = set()
        while r < len(s):
            current = 0
            if s[l] != s[r] and s[r] not in window:
                current = r - l + 1
                window.add(s[r])
                r += 1
            else:
                l += 1
                window.discard(s[l])
                if l == r:
                    r += 1
            longest = max(longest, current)

        
        if len(s) > 0:
            longest = max(longest, 1)
            
        return longest