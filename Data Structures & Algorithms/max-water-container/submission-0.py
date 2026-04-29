class Solution:
    def maxArea(self, heights: List[int]) -> int:
        answer = 0
        l, r = 0, len(heights)-1
        while l<r:
            waters = min(heights[l], heights[r])*(r-l)
            answer = max(answer, waters)
            if heights[l]>heights[r]:
                r-=1
            else: l+=1
        return answer