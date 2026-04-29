class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        l, r = 0, len(height)-1
        lm = height[l]
        rm = height[r]
        while l<r:
            if lm<rm:
                l+=1
                lm = max(lm, height[l])
                answer += lm-height[l]
            else:
                r-=1
                rm = max(rm, height[r])
                answer += rm-height[r]
        return answer