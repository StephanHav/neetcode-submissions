class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not len(edges) == (n - 1):
            return False
        
        hmap = { i:[] for i in range(n)}
        for edge in edges:
            hmap[edge[0]].append(edge[1])
            hmap[edge[1]].append(edge[0])

        visited = set([0])
        stack = [0]

        while stack:
            node = stack.pop()
            for edge in hmap[node]:
                if edge not in visited:
                    visited.add(edge)
                    stack.append(edge)

        return len(visited) == n


            
            