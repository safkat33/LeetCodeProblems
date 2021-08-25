"""
Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree_dfs(self, node, array):
        if node:
            array.append(node.val)
            if node.left:
                self.tree_dfs(node.left, array)
            else:
                array.append(node.left)
            if node.right:
                self.tree_dfs(node.right, array)
            else:
                array.append(node.right)
        return array

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_pre_order = self.tree_dfs(p, [])
        q_pre_order = self.tree_dfs(q, [])

        return p_pre_order == q_pre_order
