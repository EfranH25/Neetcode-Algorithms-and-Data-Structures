# difficulty: easy
# solution: https://neetcode.io/problems/two-integer-sum?list=neetcode150
# my solution

from typing import List, Optional

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = {}

        for idx, num in enumerate(nums):
            num_map[num] = idx

        for i in range(len(nums)):
            dif = target - nums[i]

            if dif in num_map and num_map[dif] != i:
                return [i, num_map[dif]]