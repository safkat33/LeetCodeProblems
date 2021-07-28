'''
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.



Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums)-1:
            if nums[i] != nums[i + 1]:
                res.append(nums[i])
                i += 1
                if len(res) == 2:
                    return res
            else:
                i += 2
        res.append(nums[-1])
        return res