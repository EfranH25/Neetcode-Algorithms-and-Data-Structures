# difficulty: easy
# solution: https://neetcode.io/problems/duplicate-integer?list=neetcode150
# my solution

from typing import List, Optional


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            else:
                num_set.add(n)

        return False