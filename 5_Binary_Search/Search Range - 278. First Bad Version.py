# difficulty: easy
# solution: https://leetcode.com/problems/first-bad-version/description/
# my solution

from typing import List

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L, R = 1, n

        while L <= R:
            mid = (L + R) // 2
            mid_version = isBadVersion(mid)

            if mid_version:
                # if mid == L:
                #     return False
                before_version = isBadVersion(mid-1)
                if not before_version:
                    return mid
                else:
                    R = mid - 1
            else:
                L = mid + 1
