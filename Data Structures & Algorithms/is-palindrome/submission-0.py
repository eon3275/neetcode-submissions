class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        strs = []
        for c in s:
            if c.isalnum():
                strs.append(c)
        return True if strs==strs[-1::-1] else False