# difficulty: medium
# solution: https://neetcode.io/problems/kth-largest-element-in-an-array?list=neetcode150
# my solution

from typing import List, Optional
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        result = None
        for n in nums:
            heapq.heappush(maxHeap, -n)

        for i in range(k):
            result = -heapq.heappop(maxHeap)

        return result


# built in functions
# class Solution:
#     def findKthLargest(self, nums, k):
#         return heapq.nlargest(k, nums)[-1]

# Another option is Quick Select which is a version of quick sort
# Time complexity: 𝑂 ( 𝑛 ) O(n) in average case, 𝑂 ( 𝑛 2 ) O(n 2 ) in worst case.
# Space complexity: 𝑂 ( 𝑛 ) O(n)