class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs_hmap = { i:[] for i in range(numCourses)}

        for req in prerequisites:
            reqs_hmap[req[0]].append(req[1])
        
        visited = set()
        def dfs(course):
            
            if course in visited:
                return False

            if course == []:
                return True
            
            visited.add(course)
            for neighbor in reqs_hmap[course]:
                if not dfs(neighbor):
                    return False
            
            visited.remove(course)

            return True

        for course in reqs_hmap:
            if not dfs(course):
                return False
        return True
