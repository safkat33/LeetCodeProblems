from typing import List
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        complement_map = dict()

        length = len(nums)
        for i in range(length):
            num = nums[i]
            complement = target - num
            if num in complement_map:
                return [complement_map[num], i]
            else:
                complement_map[complement] = i

    @staticmethod
    def brute_force_two_sum(nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if i == j:
                    continue
                elif nums[i] + nums[j] == target:
                    return [i, j]





