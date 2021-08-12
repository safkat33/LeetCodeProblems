'''
Binary Tree Preorder Traversal
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
        1
    2       3
4      5 6      7
Input: root = [1,2,3,4,5,6,7]
Output: [1,2,4,5,3,6,7]
'''

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getPreOrder(self, node, res):
        if node:
            res.append(node.val)
            if node.left:
                self.getPreOrder(node.left, res)
            if node.right:
                self.getPreOrder(node.right, res)
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = self.getPreOrder(root, [])
        return res
