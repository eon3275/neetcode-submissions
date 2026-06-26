class Solution: #dfs
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [0]*n
        def dfs(node):
            for c in adj[node]:
                if not visited[c]:
                    visited[c] = 1
                    dfs(c)
        res = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                res+=1
                dfs(i)
        return res