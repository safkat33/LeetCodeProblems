"""
Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkLevel(self, node, level_viewed, level, right_view):
        if not node:
            return right_view
        if len(level_viewed) <= level:
            level_viewed.append(False)
        if not level_viewed[level]:
            right_view.append(node.val)
            level_viewed[level] = True
        if node.right:
            self.checkLevel(node.right, level_viewed, level + 1, right_view)
        if node.left:
            self.checkLevel(node.left, level_viewed, level + 1, right_view)
        return right_view

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.checkLevel(root, [False], 0, [])