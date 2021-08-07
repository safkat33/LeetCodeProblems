'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''


class Solution:
    def getPalindrome(self, left_pointer, right_pointer, string_val):
        res = ""
        while left_pointer >= 0 and right_pointer < len(string_val):
            if string_val[left_pointer] == string_val[right_pointer]:
                res = string_val[left_pointer:right_pointer + 1]
                left_pointer -= 1
                right_pointer += 1
            else:
                break
        return res

    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for i in range(1, len(s)):
            sub_res = s[i]
            if i < len(s) - 1:
                # for Odd Palindrome
                if s[i - 1] == s[i + 1]:
                    sub_res = self.getPalindrome(i - 1, i + 1, s)
            res = sub_res if len(sub_res) > len(res) else res
            if i < len(s):
                # for Even Palindrome
                if s[i - 1] == s[i]:
                    sub_res = self.getPalindrome(i - 1, i, s)
            res = sub_res if len(sub_res) > len(res) else res
        return res
