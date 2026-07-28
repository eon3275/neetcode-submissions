class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_min = curr_max = 1
        for n in nums:
            curr_min, curr_max = min(n, curr_min*n, curr_max*n), max(n, curr_min*n, curr_max*n)
            res = max(res, curr_max)
        return res