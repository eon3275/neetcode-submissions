class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lis = sorted(list(zip(position, speed)), reverse=True)
        stack = []
        for p, s in lis:
            time = (target-p)/s
            if not stack or stack[-1]<time:
                stack.append(time)
        return len(stack)