# difficulty: medium
# solution: https://neetcode.io/problems/level-order-traversal-of-binary-tree?list=neetcode150
# my solution

from typing import List, Optional

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([])
        q.append(root)

        output = []

        if not root:
            return output

        while q:
            entry = []
            for i in range(len(q)):
                cur = q.popleft()
                entry.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            output.append(entry)

        return output