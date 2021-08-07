'''
67. Add Binary

Share
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # One Line Solution
        # return bin(int(a,2) + int(b,2))[2:]
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        res = ''
        carry = 0
        for i in range(1, max_len + 1):
            sum = int(a[-i]) + int(b[-i]) + carry
            if sum == 3:
                res = '1' + res
                carry = 1
            elif sum == 2:
                res = '0' + res
                carry = 1
            elif sum == 1:
                res = '1' + res
                carry = 0
            else:
                res = '0' + res
                carry = 0
        if carry == 1:
            res = '1' + res
        return res


list = [1,2,3,4,5,6,7]
print(list[::-1])