'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ["" for i in range(numRows)]
        idx = 0
        downwards = True
        for i in range(len(s)):
            rows[idx] +=  s[i]
            if downwards:
                if idx+1 < numRows:
                    idx += 1
                else:
                    downwards = False
                    idx -= 1
            else:
                if idx > 0:
                    idx -= 1
                else:
                    downwards = True
                    idx += 1
        res = ""
        for i in range(numRows):
            res += rows[i]
        return res
