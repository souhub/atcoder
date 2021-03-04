class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = set([i+1 for i in range(len(nums))])
        nums = set(nums)
        ans = list(ans-nums)
        return ans
