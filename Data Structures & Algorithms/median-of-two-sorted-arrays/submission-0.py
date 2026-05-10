class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half = (m+n)//2
        l, r = 0, m
        while l<=r:
            i = (l+r)//2
            j = half - i
            l1 = nums1[i-1] if i>0 else float('-inf')
            r1 = nums1[i] if i<m else float('inf')
            l2 = nums2[j-1] if j>0 else float('-inf')
            r2 = nums2[j] if j<n else float('inf')
            if l1<=r2 and l2<=r1:
                if (m+n)%2==1:
                    return min(r1, r2)
                else:
                    return (max(l1, l2)+min(r1,r2))/2
            elif l1>r2:
                r = i-1
            else:
                l = i+1