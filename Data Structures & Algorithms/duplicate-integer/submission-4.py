class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicts = {}
        ans = False
        for n in nums:
            if n not in dicts:
                dicts[n] = 1
            else:
                ans = True
        return ans