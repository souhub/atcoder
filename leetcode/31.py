class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        target1_index = -1
        target2_index = -1
        diff = float('inf')

        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                target1 = nums[i-1]
                target1_index = i-1
                break

        if target1_index != -1:
            for j in range(target1_index+1, len(nums)):
                if nums[j] > target1 and diff >= nums[j]-target1:
                    diff = nums[j]-target1
                    target2_index = j

            nums[target1_index], nums[target2_index] = nums[target2_index], nums[target1_index]
            print(nums)

        for k in range(target1_index+1, len(nums)-1):
            for l in range(k+1, len(nums)):
                if nums[k] > nums[l]:
                    nums[k], nums[l] = nums[l], nums[k]
