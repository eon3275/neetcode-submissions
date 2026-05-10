from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap: return ""
        values = self.tmap[key]
        l, r = 0, len(values)-1
        res = ""
        while l<=r:
            mid = (l+r)>>1
            if values[mid][0]<=timestamp:
                res = values[mid][1]
                l = mid+1
            else:
                r = mid-1
        return res
