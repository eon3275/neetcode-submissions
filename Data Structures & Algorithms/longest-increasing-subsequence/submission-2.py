class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [nums[0]]
        answer = 1
        def binary_search(target):
            l, r = 0, len(lis)-1
            while l<=r:
                mid = (l+r)//2
                if lis[mid]<target:
                    l = mid+1
                else:
                    r = mid-1
            return l
        for i in range(1, len(nums)):
            if lis[-1]<nums[i]:
                lis.append(nums[i])
            else:
                idx = binary_search(nums[i])
                lis[idx] = nums[i]
        return len(lis)