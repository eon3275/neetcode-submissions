class Solution:
    def find(self, node):
        curr = node
        while curr!=self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu==pv:
            return False
        if self.size[pv]>self.size[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.size[pu]+=self.size[pv]
        return True
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        self.parent = [i for i in range(n)]
        self.size = [1]*n
        adj = []
        for i in range(n):
            for j in range(i+1,n):
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                adj.append([i,j,dist])
        adj.sort(key=lambda x:x[2])
        res = 0
        edges = 0
        for src, dst, weight in adj:
            if self.union(src, dst):
                res+=weight
                edges+=1
            if edges==n-1: break
        return res