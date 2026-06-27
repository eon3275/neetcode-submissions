class Solution: #DSU
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        parent = [i for i in range(n+1)]
        rank = [1]*(n+1)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def find(node):
            curr = node
            while curr!=parent[curr]:
                parent[node] = parent[parent[node]]
                curr = parent[node]
            return curr
        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu==pv:
                return False
            if rank[pv]>rank[pu]:
                pu, pv = pv, pu
            parent[pv] = pu
            rank[pu]+=rank[pv]
            return True
        for u, v in edges:
            if not union(u,v):
                return [u,v]