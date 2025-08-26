# difficulty: easy
# solution: https://leetcode.com/problems/search-in-a-binary-search-tree/description/
# my solution

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def bst_search(node, val):
            if node is None:
                return None
            elif node.val == val:
                return node

            if node.val > val:
                return bst_search(node.left, val)
            else:
                return bst_search(node.right, val)

        return bst_search(root, val)