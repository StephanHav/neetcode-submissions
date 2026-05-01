class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre_map = { i:[] for i in range(numCourses)}
        for node in prerequisites:
            pre_map[node[0]].append(node[1])
        
        visit = set()

        def dfs(node):
            if node in visit:
                return False

            visit.add(node)

            for nb in pre_map[node]:
                if not dfs(nb):
                    return False

            visit.remove(node)
            return True

        for node in pre_map:
            if not dfs(node):
                return False
        
        return True

        
