class Solution: #dfs
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nextMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            nextMap[pre].append(crs)
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            elif not nextMap[crs]:
                return True
            visiting.add(crs)
            for nxt in nextMap[crs]:
                if not dfs(nxt):
                    return False
            visiting.remove(crs)
            nextMap[crs].clear()
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True