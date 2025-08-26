# difficulty: easy
# solution: https://neetcode.io/problems/remove-element?list=neetcode150
# my solution
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    pointer_1, pointer_2 = 0, 1

    while pointer_2 < len(nums):
        if nums[pointer_2] > nums[pointer_1]:
            pointer_1 += 1
            nums[pointer_1] = nums[pointer_2]
        pointer_2 += 1

    nums = nums[:pointer_1+1]

    return len(nums)


entry = [1,1,2,3,4]