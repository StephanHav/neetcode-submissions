class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        ways = 0
        one_back = 1
        two_back = 1
        for i in range(1, len(s)+1):
            num = int(s[i-1])
            ways = 0

            if num > 0:
                ways += one_back
            if i > 1:
                if 0 < int(s[i-2]) and int(s[i-2:i]) <= 26:
                    ways += two_back
            two_back = one_back
            one_back = ways
        return ways

            