class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        len_str = len(s)
        dp = [False] * (len_str + 1)
        dp[0] = True     

        for i in range(1, len(dp)):
            for word in wordDict:
                len_word = len(word)
                pre = i - len_word

                if pre >= 0 and dp[pre]:
                    if s[pre:i] == word:
                        dp[i] = True
                        break

        return dp[len_str]



            # ["catsin"]
            # ["cats","cat","sin"]
            # s = 6
            # i = 1
            # dp = [True,False,False,True,True,False,False]