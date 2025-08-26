# difficulty: easy
# solution: https://neetcode.io/problems/binary-search?list=neetcode150
# my solution

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L+R)//2

            print(L, mid, R, nums[mid], nums[L:R+1])

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1

        return -1