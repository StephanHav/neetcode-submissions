class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = []
        hmap = {}
        for i in range(len(strs)):
            key = [0] * 26
            
            #Increment element corresponding to observed letter
            for m in strs[i]:
                key[ord(m) - 97] += 1

            key = tuple(key)

            #Store original string as value of corresponding key (assumes key exists in HashMap)
            v = hmap.get(key, 0)
            if v != 0:
                v.append(strs[i])
            else:
                v = [strs[i]]
            hmap[key] = v

        #return all values of hashmap in a list.
        return list(hmap.values())

