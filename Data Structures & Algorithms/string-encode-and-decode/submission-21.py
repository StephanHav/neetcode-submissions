class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i <= (len(s)-1):

            j = s.find('#', i)
            length = int(s[i:j])
            decoded_str = s[j+1:j+1+length]
            strs.append(decoded_str)
            i = j+1+length

        return strs