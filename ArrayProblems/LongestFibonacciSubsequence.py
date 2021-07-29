'''
A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].



Example 1:

Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
'''
from typing import List


class Solution:

    def binarySearch(self, arr, l, r, val):
        if r is None:
            r = len(arr) - 1
        if l <= r:
            mid = (l + r) // 2
            if arr[mid] == val:
                return True, mid
            elif arr[mid] > val:
                return self.binarySearch(arr, l, mid - 1, val)
            else:
                return self.binarySearch(arr, mid + 1, r, val)
        else:
            return False, None

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        count = 0
        lenth = len(arr)
        for i in range(0, lenth - 2):
            if lenth - i < count:
                break
            for j in range(i + 1, lenth - 1):
                count_sub = 0
                next_val = arr[i] + arr[j]
                if arr[j + 1] > next_val:
                    continue
                old_val = arr[j]
                old_val_idx = j
                while next_val < arr[-1] + 1:
                    if arr[old_val_idx + 1] > next_val:
                        break
                    is_exist, idx = self.binarySearch(arr[old_val_idx + 1:], 0, None, next_val)
                    if is_exist:
                        if count_sub == 0:
                            count_sub += 3
                        else:
                            count_sub += 1
                        temp = next_val
                        next_val += old_val
                        old_val = temp
                        old_val_idx = idx
                    else:
                        break
                count = max(count, count_sub)
        return count


"""
[0,1,2,3,4,5,6,7,8,9]
"""


# If I use set instead of List then The program will be faster in case of searching as it can search in constant time.


def lenLongestFibSubseqSet(arr):
    count = 0
    lenth = len(arr)
    data_set = set(arr)
    for i in range(0, lenth - 2):
        if lenth - i < count:
            break
        for j in range(i + 1, lenth - 1):
            count_sub = 0
            next_val = arr[i] + arr[j]
            if arr[j + 1] > next_val:
                continue
            old_val = arr[j]
            while next_val < arr[-1] + 1:
                if arr[j + 1] > next_val:
                    break
                if next_val in data_set:
                    if count_sub == 0:
                        count_sub += 3
                    else:
                        count_sub += 1
                    next_val, old_val = old_val + next_val, next_val
                else:
                    break
            count = max(count, count_sub)
    return count


"""
[0,1,2,3,4,5,6,7,8,9]
"""
