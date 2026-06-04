import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones)>1:
            y, x = heapq.heappop(stones), heapq.heappop(stones)
            if x>y:
                heapq.heappush(stones, y-x)
        stones.append(0)
        return -stones[0]