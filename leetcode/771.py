class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for i in range(len(jewels)):
            jewels_in_stones = stones.count(jewels[i])
            ans += jewels_in_stones
        return ans
