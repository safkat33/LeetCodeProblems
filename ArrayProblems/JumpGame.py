from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        Track = [False for i in range(len(nums))]
        Track[0] = True
        for i in range(len(nums)):
            if Track[i]:
                j = nums[i] + i
                while j > i:
                    if nums[i] + i + 1 >= len(nums):
                        return True
                    Track[j] = True
                    j -= 1
        return Track[len(nums) - 1]