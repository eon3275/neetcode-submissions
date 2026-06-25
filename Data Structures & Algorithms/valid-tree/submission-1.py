class Solution: #dfs
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        for p, c in edges:
            adj[p].append(c)
            adj[c].append(p)
        visited = set()
        def dfs(parent, node):
            if node in visited:
                return False
            visited.add(node)
            for n in adj[node]:
                if n==parent:
                    continue
                if not dfs(node, n):
                    return False
            return True
        return dfs(-1,0) and len(visited)==n