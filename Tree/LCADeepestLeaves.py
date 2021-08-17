"""
Lowest Common Ancestor of Deepest Leaves
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
Note: This question is the same as 865: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def chekLevels(self, node, level_array, level):
        if node is None:
            return level_array
        if len(level_array) <= level:
            level_array.append([])
        if node not in level_array[level]:
            level_array[level].append(node)
        self.chekLevels(node.left, level_array, level + 1)
        self.chekLevels(node.right, level_array, level + 1)
        return level_array

    def findNode(self, root, node):
        if root is None:
            return False
        if root == node or self.findNode(root.left, node) or self.findNode(root.right, node):
            return True

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_array = self.chekLevels(root, [[]], 0)
        i = -1
        highest_nodes = level_array[i]
        while i:
            res_level = level_array[i]
            if len(res_level) == 1:
                return res_level[0]
            else:
                for node in res_level:
                    lca = False
                    for target in highest_nodes:
                        lca = self.findNode(node, target)
                        if not lca:
                            break
                    if lca:
                        return node
            i -= 1