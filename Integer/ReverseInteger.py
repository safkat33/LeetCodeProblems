'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
'''

class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        val = -x if x < 0 else x
        while val > 0:
            reverse = (reverse * 10) + (val % 10)
            val = val // 10
        # reverse = int(str(abs(x))[::-1]) # One Line Code
        return (-reverse if x < 0 else reverse) if reverse.bit_length() < 32 else 0
