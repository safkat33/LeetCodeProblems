"""
Maximum Product Subarray

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.


Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = None
        for i in range(len(nums)):
            sub_res = nums[i]
            temp_sub_res = nums[i]
            for j in range(i + 1, len(nums)):
                temp_sub_res *= nums[j]
                sub_res = max(sub_res, temp_sub_res)
            if res == None:
                res = sub_res
            else:
                res = max(res, sub_res)
        return res

