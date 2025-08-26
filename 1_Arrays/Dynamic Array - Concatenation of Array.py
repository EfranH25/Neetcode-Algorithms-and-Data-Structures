# difficulty: easy
# solution: https://neetcode.io/problems/concatenation-of-array?list=neetcode150
# my solution
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [0] * (2 * size)

        for idx, num in enumerate(nums):
            ans[idx] = num
            ans[size + idx] = num

        return ans

    # simpler solution via python
    def getConcatenation_simple(self, nums: List[int]) -> List[int]:
        return nums + nums