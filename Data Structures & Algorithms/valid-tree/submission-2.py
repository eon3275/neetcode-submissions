class Solution: #other dfs
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1: return False
        adj = [[] for i in range(n)]
        for p, c in edges:
            adj[p].append(c)
            adj[c].append(p)
        visited = set()
        def dfs(parent, node):
            visited.add(node)
            for c in adj[node]:
                if c==parent:
                    continue
                if c in visited:
                    return False
                if not dfs(node, c):
                    return False
            return True
        return dfs(-1,0) and len(visited)==n
                