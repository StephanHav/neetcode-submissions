class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ''

        for i in range(n - 1, -1, -1):
            for j in range(i, n):

                if s[i] == s[j]:
                    if (j - i) < 2 or dp[i+1][j-1]:
                        dp[i][j] = True

                        if len(res) < j - i + 1:
                            res = s[i:j+1]
        return res
        

