'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        res = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
                res = max(res, count)
            elif nums[i] == nums[i - 1]:
                continue
            else:
                count = 1
        return res

