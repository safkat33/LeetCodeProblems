"""
Add String

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        map_int = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        max_length = max(len(num1), len(num2))
        num1 = num1.zfill(max_length)
        num2 = num2.zfill(max_length)
        res = ''
        i = max_length - 1
        extra = 0
        while i >= 0:
            i_sum = map_int[num1[i]] + map_int[num2[i]] + extra
            res = str(i_sum % 10) + res
            extra = i_sum // 10
            i -= 1
        if extra > 0:
            res = str(extra) + res
        return res
