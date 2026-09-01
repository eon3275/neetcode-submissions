class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return 0
        ans = 0
        end = 0
        curr_end = 0
        for i in range(n-1):
            end = max(end, i+nums[i])
            if i==curr_end:
                ans+=1
                curr_end = end
                if curr_end>=n-1:
                    break
        return ans