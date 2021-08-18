"""
Maximum Product of Three Numbers

Share
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        res = None
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if res == None:
                        res = nums[i] * nums[j] * nums[k]
                    else:
                        temp = nums[i] * nums[j] * nums[k]
                        if temp > res:
                            res = temp
        return res

