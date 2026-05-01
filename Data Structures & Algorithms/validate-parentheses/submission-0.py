class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {')':'(','}':'{',']':'['}
        for c in s:
            if c not in bracket:
                stack.append(c)
            else:
                if not stack or stack.pop()!=bracket[c]:
                    return False
        return not stack