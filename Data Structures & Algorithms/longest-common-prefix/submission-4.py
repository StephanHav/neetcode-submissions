class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]

        prefix = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                
                if i < len(strs[j]) and strs[j][i] == strs[0][i] and j == (len(strs) - 1):
                    prefix = strs[0][:i+1]
                elif i < len(strs[j]) and strs[j][i] == strs[0][i]:
                    continue
                else:
                    return prefix
            
        return prefix
