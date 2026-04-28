class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for c in s:
            dict_s[c] = dict_s.get(c, 0)+1
        for c in t:
            dict_t[c] = dict_t.get(c, 0)+1
        for c in dict_s:
            if dict_s.get(c, 0)!=dict_t.get(c, 0):
                return False
        for c in dict_t:
            if dict_t.get(c, 0)!=dict_s.get(c, 0):
                return False
        return True