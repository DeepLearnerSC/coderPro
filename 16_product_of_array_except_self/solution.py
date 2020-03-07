class Solution:
  def productExceptSelf(self, nums):
    res = [1] * len(nums)
    for i in range(1, len(nums)):
      res[i] = res[i-1] * nums[i-1]
    right = 1
    for i in range(len(nums) - 2, -1, -1):
      right *= nums[i+1]
      res[i] *= right
    return res