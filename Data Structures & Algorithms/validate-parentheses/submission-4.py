class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {'}':'{', ')':'(', ']':'['}

        for c in s:
            if not stack and c not in hmap.values():
                return False
            
            elif c not in hmap.values() and stack[-1] == hmap[c]:
                stack.pop(-1)
            
            else:
                stack.append(c)


        return False if stack else True 