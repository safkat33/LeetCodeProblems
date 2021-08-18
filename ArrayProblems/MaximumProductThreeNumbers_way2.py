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
        largest_three = []
        smallest_two = []
        for i in range(len(nums)):
            if len(largest_three) < 3:
                largest_three.append(nums[i])
            else:
                smallest = min(largest_three)
                if nums[i] > smallest:
                    largest_three.remove(smallest)
                    largest_three.append(nums[i])
            if len(smallest_two) < 2:
                smallest_two.append(nums[i])
                smallest = min(smallest_two)
            else:
                smallest = min(smallest_two)
                if smallest < 0:
                    smallest = max(smallest_two)
                if nums[i] < smallest:
                    smallest_two.remove(smallest)
                    smallest_two.append(nums[i])
        product_largest = largest_three[0] * largest_three[1] * largest_three[2]
        product_with_small = max(largest_three) * smallest_two[0] * smallest_two[1] if smallest_two[0] < 0 and \
                                                                                       smallest_two[1] < 0 else 0
        return max(product_largest, product_with_small)
