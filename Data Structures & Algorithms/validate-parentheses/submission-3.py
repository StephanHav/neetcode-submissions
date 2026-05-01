class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}
        for b in s:
            if b in {'(','{','['}:
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if closeToOpen[b] != stack.pop():
                        return False

        if len(stack) > 0:
            return False
        else:
            return True 

        
        




