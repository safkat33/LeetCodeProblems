from typing import List


class Solution:
    def checkRepeat(self, nums, i):
        if i < len(nums):
            if nums[i] != nums[i-1]:
                return
            else:
                nums.remove(nums[i])
                return self.checkRepeat(nums, i)
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            self.checkRepeat(nums, i)
        return len(nums)