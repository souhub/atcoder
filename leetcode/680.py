class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                word1 = s[:l]+s[l+1:]
                word2 = s[:r]+s[r+1:]
                return word1 == word1[::-1] or word2 == word2[::-1]
            l += 1
            r -= 1
        return True
