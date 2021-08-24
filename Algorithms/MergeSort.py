from typing import List


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left_array = merge_sort(nums[:mid])
    right_array = merge_sort(nums[mid:])

    return merge(left_array, right_array)


"""
[1,2,7,8,9][3,4,5,6]
"""


def merge(left, right):
    temp = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            temp.append(left[0])
            left.remove(left[0])
        else:
            temp.append(right[0])
            right.remove(right[0])
    if len(left) > 0:
        for i in left:
            temp.append(i)
    if len(right) > 0:
        for i in right:
            temp.append(i)
    return temp


def sort(nums):
    return merge_sort(nums)


class Solution:
    print(sort([3, 1, 5, 6, 7, 8, 9, 2, 10]))


"""
[3,5,2,1,3,7,4,9]

"""


class Solution2:
    def mergeSort(self, array):
        if len(array) == 1:
            return array
        mid = len(array) // 2
        left_array = self.mergeSort(array[:mid])
        right_array = self.mergeSort(array[mid:])

        return self.merge(left_array, right_array)

    def merge(self, left_array, right_array):
        merged_array = []
        length_left = len(left_array)
        length_right = len(right_array)
        i = j = 0
        while i < length_left and j < length_right:
            if left_array[0] <= right_array[0]:
                merged_array.append(left_array[0])
                left_array.pop(0)
                i += 1
            else:
                merged_array.append(right_array[0])
                right_array.pop(0)
                j += 1
        if i < length_left:
            merged_array += left_array
        if j < length_right:
            merged_array += right_array
        return merged_array

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
