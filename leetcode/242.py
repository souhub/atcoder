class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        else:
            if sorted(s) == sorted(t):
                return True
        return False
