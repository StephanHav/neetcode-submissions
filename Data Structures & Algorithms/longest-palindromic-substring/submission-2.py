class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(l, r):

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l+1: r]
        
        res = ''
        for i in range(len(s)):
            even = expand(i, i+1)
            uneven = expand(i-1, i+1)

            if len(even) > len(res):
                res = even
            
            if len(uneven) > len(res):
                res = uneven
        
        return res


        # def isPalindrome(substr):
        #     l = 0
        #     r = len(substr) - 1
        #     mid = len(substr) // 2
        #     for _ in range(mid):
        #         if substr[l] != substr[r]:
        #             return False
        #         else:
        #             l += 1
        #             r -= 1
        #     return True

        # max_pal = 0
        # res = ''
        # for i in range(len(s)):
        #     for j in range(i, len(s) + 1):
        #         if isPalindrome(s[i:j]):
        #             max_pal = max(max_pal, len(s[i:j]))
        #             if len(s[i:j]) == max_pal:
        #                 res = s[i:j]
        # return res

