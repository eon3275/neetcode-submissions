class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ind = [0]*numCourses
        adj = [[] for i in range(numCourses)]
        res = []
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
            res.append(node)
            for n in adj[node]:
                ind[n]-=1
                if ind[n]==0:
                    q.append(n)
        return res if finished==numCourses else []