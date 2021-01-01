class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        sx = str(x)
        n = 0
        for i in range(len(sx)-1, -1, -1):
            n += int(sx[i])*10**i
        if n == x:
            return True
