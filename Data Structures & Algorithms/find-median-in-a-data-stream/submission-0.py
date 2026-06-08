class MedianFinder:

    def __init__(self):
        self.left_max = []
        self.right_min = []

    def addNum(self, num: int) -> None:
        if len(self.left_max)==len(self.right_min):
            heapq.heappush(self.left_max, -heapq.heappushpop(self.right_min, num))
        else:
            heapq.heappush(self.right_min, -heapq.heappushpop(self.left_max, -num))


    def findMedian(self) -> float:
        if len(self.left_max)==len(self.right_min):
            return (-self.left_max[0]+self.right_min[0])/2
        else:
            return -self.left_max[0]        