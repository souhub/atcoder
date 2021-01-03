# 全探索
# Time over

# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         max_total = float('-inf')
#         for i in range(len(nums)):
#             s = 0
#             g = i+1
#             for _ in range(len(nums)-1, -1, -1):
#                 total = 0
#                 for j in range(s, g):
#                     total += nums[j]
#                 if max_total < total:
#                     max_total = total
#                 s += 1
#                 g += 1
#                 if len(nums) < g:
#                     break
#         return max_total


# Kadane's algorithm(Dynamic programming)


# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         max_sum, curr_sum = nums[0], 0
#         for i in nums:
#             if curr_sum < 0:
#                 curr_sum = 0
#             curr_sum += i
#             max_sum = max(max_sum, curr_sum)
#         return max_sum


# h = [2, 9, 4, 5, 1, 6, 10]
# ans = 0
# dp = [float('inf') for _ in range(len(h))]
# # a[n]=a[n-1]+a[n-2]


# # when n=0,1
# dp[0] = 0
# dp[1] = 7
# # when n>=2
# for n in range(2, len(dp)):
#     dp[n] = min(dp[n-1]+abs(h[n]-h[n-1]), dp[n-2]+abs(h[n]-h[n-2]))
# print(dp, dp[len(h)-1])

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

dp = [float('-inf') for _ in range(len(nums))]

dp[0] = nums[0]
for n in range(1, len(nums)):
    dp[n] = max(dp[n-1]+nums[n], dp[n-1])
print(dp[len(nums)-1], dp)
