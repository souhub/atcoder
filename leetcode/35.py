class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        is_found = False
        is_inserted = False
        ans = -1
        for i in range(len(nums)):
            if nums[i] == target:
                is_found = True
                ans = i
        if is_found:
            return ans
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    is_inserted = True
                    ans = i
                    break
            if is_inserted:
                return ans
            else:
                ans = len(nums)
                return ans
