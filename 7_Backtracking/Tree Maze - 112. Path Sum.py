# difficulty: easy
# solution: https://leetcode.com/problems/path-sum/description/
# my solution

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def search(node, total, target):
            if not node:
                return False

            print(node.val)
            # check leaf
            if not node.left and not node.right:
                print("------", total + node.val)
                if total + node.val == target:
                    return True
                else:
                    return False

            total += node.val
            print(total, node.val, target)
            # if total > target:
            #     print("fail")
            #     return False

            if search(node.left, total, target):
                print("left")
                return True

            if search(node.right, total, target):
                print("right")
                return True


            print("all done")
            return False

        result = search(root, 0, targetSum)
        return result