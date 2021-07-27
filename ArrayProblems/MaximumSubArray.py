from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < nums[i] + nums[i - 1]:
                nums[i] = nums[i] + nums[i - 1]
            max_sum = max(nums[i], max_sum)
        return max_sum
