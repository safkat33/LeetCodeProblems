"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:

Input: num = 3
Output: "III"
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        if num >= 1000:
            for i in range(num//1000):
                res += "M"
            num %= 1000
        if num >= 900:
            res += "CM"
            num %= 900
        if num >= 500:
            for i in range(num//500):
                res += "D"
            num %= 500
        if num >= 400:
            res += "CD"
            num %= 400
        if num >= 100:
            for i in range(num//100):
                res += "C"
            num %= 100
        if num >= 90:
            res += "XC"
            num %= 90
        if num >= 50:
            for i in range(num//50):
                res += "L"
            num %= 50
        if num >= 40:
            res += "XL"
            num %= 40
        if num >= 10:
            for i in range(num//10):
                res += "X"
            num %= 10
        if num == 9:
            res += "IX"
            num -= 9
        if 4 < num < 9:
            res += "V"
            num -= 5
            for i in range(num):
                res += "I"
                num -= 1
        if num == 4:
            res += "IV"
            num -= 4
        if num < 4:
            for i in range(num):
                res += "I"
                num -= 1
        return res