class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId])>10:
            self.tweetMap[userId].pop(0)
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        self.followMap[userId].add(userId)
        for uid in self.followMap[userId]:
            if self.tweetMap[uid]:
                last_idx = len(self.tweetMap[uid])-1
                time, tid = self.tweetMap[uid][-1]
                heap.append([time, tid, uid, last_idx-1])
        heapq.heapify(heap)
        while heap and len(res)<10:
            time, tid, uid, next_idx = heapq.heappop(heap)
            res.append(tid)
            if next_idx>=0:
                time, tid = self.tweetMap[uid][next_idx]
                heapq.heappush(heap, [time, tid, uid, next_idx-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
