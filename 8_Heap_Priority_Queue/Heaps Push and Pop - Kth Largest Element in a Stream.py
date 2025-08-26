# difficulty: easy
# solution: https://neetcode.io/problems/kth-largest-integer-in-a-stream?list=neetcode150
# my solution

from typing import List, Optional

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        k_largest = heapq.nlargest(self.k, self.nums)
        return k_largest[-1]
