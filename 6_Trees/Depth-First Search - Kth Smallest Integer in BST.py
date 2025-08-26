# difficulty: medium
# solution: https://neetcode.io/problems/kth-smallest-integer-in-bst?list=neetcode150
# my solution

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, count):
            if node is None:
                return None, count

            result, count = dfs(node.left, count)
            count -= 1
            if count <= 0:
                if result is None:
                    result = node.val
                return result, count
            return dfs(node.right, count)


        result, count = dfs(root, k)

        return result