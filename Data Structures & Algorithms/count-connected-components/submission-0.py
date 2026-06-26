class Solution: #bfs
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [0]*n
        def bfs(node):
            q = deque([node])
            while q:
                curr = q.popleft()
                for c in adj[curr]:
                    if not visited[c]:
                        visited[c] = 1
                        q.append(c)
        res = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                res+=1
                bfs(i)
        return res