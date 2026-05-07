class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0]*n
        right = [n-1]*n
        stack = []
        for i in range(n):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if stack: left[i] = stack[-1]+1
            stack.append(i)
        stack.clear()
        for i in range(n-1, -1, -1):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if stack: right[i] = stack[-1]-1
            stack.append(i)
        max_value = 0
        for i in range(n):
            max_value = max(max_value, heights[i]*(right[i]-left[i]+1))
        return max_value