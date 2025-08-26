# difficulty: easy
# solution: https://neetcode.io/problems/binary-tree-inorder-traversal?list=neetcode150
# my solution

from typing import List, Optional



# Definition for a binary tree node.
# Note: performance can be improved regarding space
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inorder(node, output):
            if not node:
                return output

            output = inorder(node.left, output)
            output.append(node.val)
            output = inorder(node.right, output)
            return output

        output = inorder(root, [])
        return output