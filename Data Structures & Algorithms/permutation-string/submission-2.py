class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_map = {}
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1
        
        window = len(s1)
        ptr = window

        while ptr <= len(s2):
            s1_map_cp = s1_map.copy()
            for c in s2[ptr-window:ptr]:
                
                if c in s1_map_cp:
                    s1_map_cp[c] = s1_map_cp.get(c, 0) - 1
                    correct = 0
                    for key in s1_map_cp:
                        if s1_map_cp[key] != 0:
                            break
                        else:
                            correct += 1
                            if correct == len(s1_map):
                                return True
                else:
                    break
            ptr += 1

        return False