class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        index = 0

        # numbers=[i for i in nums if i!=0] This was failed because of changing id of nums

        for i in range(len_nums):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1

        for j in range(index, len_nums):
            nums[j] = 0
