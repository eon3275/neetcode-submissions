class Solution: #khan's
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        ind = [0]*(n+1)
        q = deque()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            ind[u]+=1
            ind[v]+=1
        for i in range(n+1):
            if ind[i]==1:
                q.append(i)
        while q:
            curr = q.popleft()
            ind[curr]-=1
            for nei in adj[curr]:
                ind[nei]-=1
                if ind[nei]==1:
                    q.append(nei)
        for u, v in reversed(edges):
            if ind[u]==ind[v]==2:
                return [u,v]
        return []