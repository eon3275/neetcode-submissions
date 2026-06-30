class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        visited = set()
        heap = [(0, k)]
        t = 0
        while heap:
            c_w, c_n = heapq.heappop(heap)
            if c_n in visited:
                continue
            visited.add(c_n)
            t = c_w
            for nxt_n, nxt_w in adj[c_n]:
                if nxt_n not in visited:
                    heapq.heappush(heap, (c_w+nxt_w,nxt_n))
        return t if len(visited)==n else -1