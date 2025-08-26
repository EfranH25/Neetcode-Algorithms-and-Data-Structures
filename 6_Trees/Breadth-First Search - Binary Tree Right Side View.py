# difficulty: easy
# solution: https://neetcode.io/problems/binary-tree-right-side-view?list=neetcode150
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        if not root:
            return output

        q = deque([])
        q.append(root)

        level = 0

        while q:
            print(level)
            for i in range(len(q)):
                cur = q.popleft()
                if i == 0:
                    output.append(cur.val)
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)

            level += 1

        return output