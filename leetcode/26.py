class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j += 1
                cnt += 1
                nums[j] = nums[i]
        return cnt
