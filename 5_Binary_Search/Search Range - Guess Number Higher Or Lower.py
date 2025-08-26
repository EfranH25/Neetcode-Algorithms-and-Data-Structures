# difficulty: easy
# solution: https://neetcode.io/problems/guess-number-higher-or-lower?list=neetcode150
# my solution

from typing import List

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L, R = 1, n

        while L <= R:
            mid = (L + R) // 2
            print(L, mid, R)
            if guess(mid) == 0:
                return mid
            elif guess(mid) < 0:
                R = mid - 1
            else:
                L = mid + 1

        return mid
