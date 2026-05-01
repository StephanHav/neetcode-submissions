class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not len(edges) == (n - 1):
            return False
        
        hmap = { i:[] for i in range(n)}
        for edge in edges:
            hmap[edge[0]].append(edge[1])
            hmap[edge[1]].append(edge[0])

        not_seen = set(list(range(n)))

        def dfs(node):
            if node not in not_seen:
                return False
            else:
                not_seen.remove(node)
            
            if hmap[node] == []:
                return True
            
            for edge in hmap[node]:
                dfs(edge)
            
            return True 
        
        if not dfs(0):
            return False
        
        return len(not_seen) == 0


            
            