class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        answer = r
        while l<=r:
            mid = (l+r)>>1
            cnt = 0
            for b in piles:
                cnt += (b+mid-1)//mid
            if cnt>h:
                l = mid+1
            else:
                answer = mid
                r = mid-1
        return answer