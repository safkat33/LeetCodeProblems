'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_array = nums1 + nums2
        final_array.sort()
        lenth = len(final_array)
        if lenth%2 == 0:
            i = lenth//2
            j = i-1
            sum = final_array[i]+final_array[j]
            if sum > 0:
                return sum/2
            return 0
        else:
            return final_array[lenth//2]