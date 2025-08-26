# difficulty: medium
# solution: https://neetcode.io/problems/insert-into-a-binary-search-tree?list=neetcode150
# my solution

from typing import List, Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# big O for Space is O(n) due too call stack of recursion
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def insert(node, val):
            if node is None:
                return TreeNode(val)

            if node.val > val:
                node.left = insert(node.left, val)
            elif node.val < val:
                node.right = insert(node.right, val)

            return node


        return insert(root, val)


# Better solution --> big O for Space is O(1)
# Definition for a binary tree node.
class Solution_2:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        cur = root

        while True:
            if cur.val > val:
                if cur.left is None:
                    cur.left = TreeNode(val)
                    break
                cur = cur.left
            if cur.val <= val:
                if cur.right is None:
                    cur.right = TreeNode(val)
                    break
                cur = cur.right
        return root