class Solution: #DSU
    def find(self, curr):
        while curr!=self.parent[curr]:
            self.parent[curr]=self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu!=pv:
            if self.rank[pv]>self.rank[pu]:
                pu,pv = pv,pu
            self.parent[pv]=pu
            self.rank[pu]+=pv
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        self.parent = [i for i in range(n*n)]
        self.rank = [1]*(n*n)
        pos = []
        for r in range(n):
            for c in range(n):
                pos.append((grid[r][c],r,c))
        pos.sort()
        dydx = [[1,0],[-1,0],[0,1],[0,-1]]
        for h,r,c in pos:
            for dy, dx in dydx:
                ny,nx = r+dy,c+dx
                if 0<=ny<n and 0<=nx<n and h>grid[ny][nx]:
                    src = ny*n+nx
                    dst = r*n+c
                    self.union(src, dst)
            if self.find(0)==self.find(n*n-1):
                return h
        return -1