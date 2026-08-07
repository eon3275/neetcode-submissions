class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = ans = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], nums[i]+curr_sum)
            ans = max(ans, curr_sum)
        return ans