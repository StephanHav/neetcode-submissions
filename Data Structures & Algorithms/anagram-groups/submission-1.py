from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = defaultdict(list)
        for s in strs:
            key = [0] * 26
            
            #Increment element corresponding to observed letter
            for m in s:
                key[ord(m) - ord('a')] += 1

            key = tuple(key)
            hmap[key].append(s)

        #return all values of hashmap in a list.
        return list(hmap.values())

