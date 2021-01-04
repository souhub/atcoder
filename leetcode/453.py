# Solution 1
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        check = True
        cnt = 0

        count_of_incrementing = len(nums)-1

        if count_of_incrementing <= 0:
            return cnt

        while True:
            nums.sort()

            for i in range(len(nums)-1):
                if nums[i] == nums[i+1]:
                    continue
                else:
                    check = False

            if check is True:
                break

            for i in range(count_of_incrementing):
                nums[i] += 1

            cnt += 1
            check = True

        return cnt


# Solution 2
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        check = True
        cnt = 0

        count_of_incrementing = len(nums)-1

        if count_of_incrementing <= 0:
            return cnt

        while True:
            nums.sort()

            for i in range(len(nums)-1):
                if nums[i] == nums[i+1]:
                    continue
                else:
                    check = False

            if check is True:
                break

            max_num = max(nums)
            min_num = min(nums)
            d = max_num-min_num

            for i in range(count_of_incrementing):
                nums[i] += d

            cnt += d
            check = True

        return cnt

# Solution 3


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        check = True
        cnt = 0

        if count_of_incrementing <= 0:
            return cnt

        nums.sort()

        while True:

            for i in range(len(nums)-1):
                if nums[i] == nums[i+1]:
                    continue
                else:
                    check = False

            if check is True:
                break

            max_num = max(nums)
            min_num = min(nums)
            d = max_num-min_num

            for i in range(len(nums)-1):
                nums[i] += d

            nums.pop()
            cnt += d
            check = True

        return cnt
