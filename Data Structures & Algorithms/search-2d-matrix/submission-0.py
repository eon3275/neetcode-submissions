class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n-1
        while l<=r:
            mid = (l+r)>>1
            row, col = divmod(mid, n)
            value = matrix[row][col]
            if value == target: return True
            elif value>target: r = mid-1
            else: l = mid+1
        return False