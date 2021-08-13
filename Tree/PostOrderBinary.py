'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.


Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]
'''

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getPostOrder(self, node, res):
        if node:
            if node.left:
                self.getPostOrder(node.left, res)
            if node.right:
                self.getPostOrder(node.right, res)
            res.append(node.val)
        return res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = self.getPostOrder(root, [])
        return res
