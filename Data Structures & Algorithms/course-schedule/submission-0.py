class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0]*numCourses
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            ind[crs]+=1
        q = deque()
        for i in range(numCourses):
            if ind[i]==0:
                q.append(i)
        finished = 0
        while q:
            node = q.popleft()
            finished+=1
            for nxt in adj[node]:
                ind[nxt]-=1
                if ind[nxt]==0:
                    q.append(nxt)
        return finished==numCourses