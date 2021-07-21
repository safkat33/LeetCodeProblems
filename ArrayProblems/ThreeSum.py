"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pair_sum_map = dict()
        result_list = []
        length = len(nums)
        if length < 3:
            return []
        nums.sort()
        for i in range(length - 2):
            if i > 2 and nums[i] == nums[i - 2]:
                continue
            else:
                for j in range(i + 1, length - 1):
                    if j > 3 and nums[j] == nums[j - 2]:
                        continue
                    else:
                        sum_i_j = nums[i] + nums[j]
                        if sum_i_j not in pair_sum_map:
                            pair_sum_map[sum_i_j] = [i, j]
                if len(pair_sum_map) > 0:
                    for k in range(length):
                        complement = 0 - nums[k]
                        if complement in pair_sum_map:
                            if pair_sum_map[complement][0] != pair_sum_map[complement][1] \
                                    and pair_sum_map[complement][0] != k and pair_sum_map[complement][1] != k:
                                result = sorted(
                                    [nums[pair_sum_map[complement][0]], nums[pair_sum_map[complement][1]], nums[k]])
                                if result not in result_list:
                                    result_list.append(result)
                    pair_sum_map.clear()
        return result_list
