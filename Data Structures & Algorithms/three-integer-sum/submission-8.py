class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]: continue
            j=i+1
            k=len(nums)-1
            target = -nums[i]
            while j<k:
                curr_sum = nums[j]+nums[k]
                if curr_sum<target:
                    j+=1
                elif curr_sum>target:
                    k-=1
                else:
                    answer.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    k-=1
        return answer