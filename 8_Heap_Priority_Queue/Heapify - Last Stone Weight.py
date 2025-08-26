# difficulty: easy
# solution: https://neetcode.io/problems/last-stone-weight?list=neetcode150
# my solution

from typing import List, Optional

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)
            if x == y:
                continue
            elif x > y:
                new_stone = x - y
                heapq.heappush(stones, -1 * new_stone)

        if stones:
            return -stones[0]

        return 0