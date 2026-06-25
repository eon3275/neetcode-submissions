class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1: return False
        adj = [[] for i in range(n)]
        for p, c in edges:
            adj[p].append(c)
            adj[c].append(p)
        visited = set()
        visited.add(0)
        q = deque([(-1, 0)])
        while q:
            parent, node = q.popleft()
            for c in adj[node]:
                if c==parent:
                    continue
                if c in visited:
                    return False
                visited.add(c)
                q.append((node, c))
        return len(visited)==n