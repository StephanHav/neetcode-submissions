class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''
        if t == s: return t
        if t == '' or s == '': return ''

        t_hmap = {}
        for i in t:
            t_hmap[i] = t_hmap.get(i, 0) + 1
        
        window = {}
        smallest = float("inf")	
        res = ''

        l = 0
        r = 0
        have = 0
        need = len(t_hmap)
        while r < len(s):
            if s[r] not in t_hmap:
                r += 1
            else:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == t_hmap[s[r]]:
                    have += 1
                r += 1
                while have == need:
                    frame = r + 1 - l
                    if frame < smallest:
                        smallest = frame
                        res = s[l:r]
                    if s[l] not in t_hmap:
                        l += 1
                    else: 
                        window[s[l]] = window.get(s[l], 0) - 1
                        if window[s[l]] < t_hmap[s[l]]:
                            have -= 1
                        l += 1
        return res


        