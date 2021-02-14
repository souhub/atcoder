class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            if nums.count(nums[i]) != 1:
                ans = nums[i]
                break
        return ans
