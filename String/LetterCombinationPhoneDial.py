"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        xs = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            for i in xs[digits[0]]:
                res.append(i)
        elif len(digits) == 2:
            for i in xs[digits[0]]:
                for j in xs[digits[1]]:
                    res.append(i+j)
        elif len(digits) == 3:
            for i in xs[digits[0]]:
                for j in xs[digits[1]]:
                    for k in xs[digits[2]]:
                        res.append(i+j+k)
        elif len(digits) == 4:
            for i in xs[digits[0]]:
                for j in xs[digits[1]]:
                    for k in xs[digits[2]]:
                        for l in xs[digits[3]]:
                            res.append(i+j+k+l)
        return res