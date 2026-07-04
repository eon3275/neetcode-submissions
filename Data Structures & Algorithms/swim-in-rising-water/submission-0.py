class Solution: #dijkstra
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0],0,0)]
        visited = set([(0,0)])
        dydx = [[1,0],[-1,0],[0,1],[0,-1]]
        while heap:
            max_t, r, c = heapq.heappop(heap)
            if r==n-1 and c==n-1:
                return max_t
            for dy, dx in dydx:
                ny,nx = r+dy, c+dx
                if 0<=ny<n and 0<=nx<n and (ny,nx) not in visited:
                    visited.add((ny,nx))
                    next_t = max(grid[ny][nx], max_t)
                    heapq.heappush(heap,(next_t,ny,nx))
        return -1