'''

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
        1
    2       3
4      5 6      7
Input: root = [1,2,3,4,5,6]
Output: [4,2,5,1,6,3,7]
'''

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getInOrder(self, node, res):
        if node:
            if node.left:
                self.getInOrder(node.left, res)
            res.append(node.val)
            if node.right:
                self.getInOrder(node.right, res)
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = self.getInOrder(root, [])
        return res
